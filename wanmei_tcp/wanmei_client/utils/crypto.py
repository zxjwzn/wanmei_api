import math
from Crypto.Cipher import AES
import binascii

class CryptoUtils:
    aesKey = [
        "e10adc3949ba5e10adc3949bae10a#>!$!%(@^4302355bbe56e057f20f883e59abbe56e057f20f883e9abbe56e057f20f883e",
        "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",
    ]
    @staticmethod
    def PVPEncrypt(data, key):
        """
        PVP加密方法，对应JS的PVPEncrypt
        :param data: 要加密的数据（二进制或字符串）
        :param key: 密钥
        :return: 加密后的二进制数据
        """
        # 确保data是二进制
        if isinstance(data, str):
            data = data.encode('latin1')  # 使用latin1以保持与JS中"binary"编码一致
        
        # 计算填充长度
        data_len = len(data)
        block_size = 16
        padded_size = math.ceil(data_len / block_size) * block_size
        padding_len = padded_size - data_len
        
        # 创建填充后的数据
        padded_data = bytearray(data)
        padded_data.extend(b'\x00' * padding_len)
        
        # 加密
        encrypted = CryptoUtils.Encrypt(padded_data, key, "")
        encrypted_binary = binascii.unhexlify(encrypted)
        
        # 构造结果：填充长度(16进制，2字符)+加密数据
        padding_hex = f"0{padding_len:x}".upper()
        result = padding_hex.encode('latin1') + encrypted_binary
        
        # 将结果转为二进制
        return CryptoUtils.Hexstring2btye(result.decode('latin1').upper())
    
    @staticmethod
    def PVPDecrypt(data, key):
        """
        PVP解密方法，对应JS的PVPDecrypt
        :param data: 要解密的二进制数据
        :param key: 密钥
        :return: 解密后的数据
        """
        # 转为十六进制字符串
        hex_str = CryptoUtils.Bytes2HexString(data)
        return CryptoUtils.HexAesDecrypt(hex_str, key)
    
    @staticmethod
    def HexAesDecrypt(hex_str, key):
        """
        十六进制AES解密，对应JS的HexAesDecrypt
        :param hex_str: 十六进制字符串
        :param key: 密钥
        :return: 解密后的数据
        """
        return CryptoUtils.Decrypt(hex_str[2:], key, "")
    
    @staticmethod
    def Decrypt(hex_str, key, iv=""):
        """
        AES解密，对应JS的Decrypt
        :param hex_str: 十六进制字符串
        :param key: 密钥
        :param iv: 初始向量（这里不使用）
        :return: 解密后的二进制数据
        """
        if isinstance(key, str):
            key = key.encode('utf-8')
            
        # 创建解密器
        cipher = AES.new(key, AES.MODE_ECB)
        
        # 解密数据
        encrypted_data = binascii.unhexlify(hex_str)
        decrypted_data = cipher.decrypt(encrypted_data)
        
        return decrypted_data.decode('latin1')
    
    @staticmethod
    def Encrypt(data, key, iv=""):
        """
        AES加密，对应JS的Encrypt
        :param data: 要加密的数据
        :param key: 密钥
        :param iv: 初始向量（这里不使用）
        :return: 加密后的十六进制字符串
        """
        if isinstance(key, str):
            key = key.encode('utf-8')
            
        if isinstance(data, str):
            data = data.encode('utf-8')
            
        # 创建加密器
        cipher = AES.new(key, AES.MODE_ECB)
        
        # 加密数据
        encrypted_data = cipher.encrypt(data)
        
        # 转为十六进制
        return binascii.hexlify(encrypted_data).decode('ascii')
    
    @staticmethod
    def Hexstring2btye(hex_str):
        """
        将十六进制字符串转换为字节，对应JS的Hexstring2btye
        :param hex_str: 十六进制字符串
        :return: 字节数组
        """
        result = bytearray()
        i = 0
        while i < len(hex_str):
            if i + 2 <= len(hex_str):
                byte_val = int(hex_str[i:i+2], 16)
                result.append(byte_val)
            i += 2
        return bytes(result)
    
    @staticmethod
    def Bytes2HexString(data):
        """
        将字节转换为十六进制字符串，对应JS的Bytes2HexString
        :param data: 字节数据
        :return: 十六进制字符串
        """
        return binascii.hexlify(data).decode('ascii')