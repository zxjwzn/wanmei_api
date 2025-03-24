import struct
from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TTransport import TFramedTransport, TMemoryBuffer
# Int64处理工具类
class Int64Utils:
    @staticmethod
    def toDecimalString(buf):
        """
        将二进制缓冲区中的64位整数转换为十进制字符串
        """
        if isinstance(buf, bytes):
            # 如果是bytes类型，转换为bytearray
            buf_array = bytearray(buf)
            offset = 0
        else:
            # 假设是具有buffer和offset属性的对象
            buf_array = buf.buffer
            offset = buf.offset
        
        # 检查是否是负数(第一个字节的最高位)
        if (buf_array[offset] != 0 or (buf_array[offset + 1] & 0xE0)) and \
            (~buf_array[offset] != 0 or ~(buf_array[offset + 1] & 0xE0) != 0):
            is_negative = (buf_array[offset] & 0x80) != 0
            
            if is_negative:
                # 对负数进行二进制补码转换
                new_buf = bytearray(8)
                has_carried = False
                
                for p in range(7, -1, -1):
                    new_buf[p] = (~buf_array[offset + p] + (0 if has_carried else 1)) & 0xFF
                    has_carried |= (buf_array[offset + p] != 0)
                
                buf_array = new_buf
            
            # 计算高16位
            high16 = buf_array[offset + 1] + (buf_array[offset] << 8)
            
            # 计算低位部分
            power_2_24 = 2**24
            power_2_32 = 2**32
            power_10_11 = 10**11
            
            low_part = buf_array[offset + 7] + \
                      (buf_array[offset + 6] << 8) + \
                      (buf_array[offset + 5] << 16) + \
                      buf_array[offset + 4] * power_2_24 + \
                      (buf_array[offset + 3] + (buf_array[offset + 2] << 8)) * power_2_32 + \
                      74976710656 * high16
            
            # 计算高位部分
            high_part = (low_part // power_10_11) + 2814 * high16
            
            # 格式化低位部分为11位数字
            low_part = str(low_part % power_10_11).zfill(11)
            
            # 组合结果
            return ("-" if is_negative else "") + str(high_part) + low_part
        
        # 如果不需要特殊处理，直接返回字符串表示
        if isinstance(buf, bytes):
            # 从8字节buffer中读取int64
            val, = struct.unpack('!q', buf[offset:offset+8])
            return str(val)
        else:
            # 从8字节buffer中读取int64
            val, = struct.unpack('!q', buf[offset:offset+8])
            return str(val)

    @staticmethod
    def fromDecimalString(decimal_str):
        """
        将十进制字符串转换为64位整数的二进制表示
        """
        # 检查是否是负数
        is_negative = decimal_str.startswith('-')
        
        # 移除负号
        if is_negative:
            decimal_str = decimal_str[1:]
        
        # 检查长度是否在范围内
        if len(decimal_str) < 16:
            # 对于较小的数字，直接使用int转换并打包成bytes
            value = int(decimal_str)
            if is_negative:
                value = -value
            return struct.pack('!q', value)
        
        if len(decimal_str) > 19:
            raise ValueError(f"Too many digits for Int64: {decimal_str}")
        
        # 分割高位和低位(高位是除了低15位的所有位)
        high_digits = decimal_str[:-15]
        low_digits = decimal_str[-15:]
        
        high_value = int(high_digits)
        low_value = int(low_digits) + 2764472320 * high_value
        
        # 计算高32位和低32位
        power_2_32 = 2**32
        high32 = (low_value // power_2_32) + 232830 * high_value
        low32 = low_value % power_2_32
        
        # 检查是否超出Int64范围
        if high32 >= 2**31 and (not is_negative or high32 != 2**31 or low32 != 0):
            raise ValueError("The magnitude is too large for Int64.")
        
        # 对于负数，执行二进制补码转换
        if is_negative:
            high32 = ~high32 & 0xFFFFFFFF
            if low32 == 0:
                high32 = (high32 + 1) & 0xFFFFFFFF
            else:
                low32 = (1 + ~low32) & 0xFFFFFFFF
            high32 |= 0x80000000  # 设置符号位
        
        # 打包成8字节
        return struct.pack('!II', high32, low32)


# 扩展TBinaryProtocol，处理I64特殊情况
class ExtendedBinaryProtocol(TBinaryProtocol):
    def __init__(self, trans, strictRead=False, strictWrite=True):
        super(ExtendedBinaryProtocol, self).__init__(trans, strictRead, strictWrite)
    
    def readI64(self):
        buff = self.trans.readAll(8)
        return Int64Utils.toDecimalString(buff)
    
    def writeI64(self, val):
        if isinstance(val, str):
            buff = Int64Utils.fromDecimalString(val)
            self.trans.write(buff)
        else:
            # 如果已经是数字，使用标准方法
            buff = struct.pack('!q', val)
            self.trans.write(buff)

class Serializer:
    @staticmethod
    def serializeBinary(obj):
        transport = TMemoryBuffer()
        protocol = ExtendedBinaryProtocol(transport)
        
        obj.write(protocol)
        protocol.trans.flush()
        return transport.getvalue()
    
    @staticmethod
    def deserializeBinary(data, objType):
        transport = TFramedTransport(data)
        protocol = ExtendedBinaryProtocol(transport)
        obj = objType()
        obj.read(protocol)
        return obj