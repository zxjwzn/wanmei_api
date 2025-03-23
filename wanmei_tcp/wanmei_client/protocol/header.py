import struct
from enum import IntEnum
# ---------------------------
# 消息包头（48字节）的实现
# ---------------------------
class MessageHeader:
    HEAD_SIZE = 48  # 固定包头大小

    def __init__(
        self, length=0,
        flag=0,
        type=0,
        reserved=0,
        source=0,
        destination=0,
        sequence=0,
        attach_id1=0,
        attach_id2=0
    ):
        self.length = length            # 4字节：整个消息包总长（不含前面4字节长度字段时也应如此）
        self.flag = flag                # 2字节
        self.type = type                # 2字节
        self.reserved = reserved        # 8字节
        self.source = source            # 8字节
        self.destination = destination  # 8字节
        self.sequence = sequence        # 4字节
        self.attach_id1 = attach_id1    # 4字节
        self.attach_id2 = attach_id2    # 8字节

    def serialize(self) -> bytes:
        return struct.pack(
            '>IHHQQQIIQ',
            self.length,
            self.flag,
            self.type,
            self.reserved,
            self.source,
            self.destination,
            self.sequence,
            self.attach_id1,
            self.attach_id2
            )

    def deserialize(self, data: bytes):
        fields = struct.unpack('>IHHQQQIIQ', data)
        self.length = fields[0]
        self.flag = fields[1]
        self.type = fields[2]
        self.reserved = fields[3]
        self.source = fields[4]
        self.destination = fields[5]
        self.sequence = fields[6]
        self.attach_id1 = fields[7]
        self.attach_id2 = fields[8]

# 基于JavaScript登录模块的LoginInfo类

class LoginType(IntEnum):
    STEAMID = 1  # 假设值基于上下文，如有需要请调整

class LoginInfo:
    def __init__(self):
        self.encrypt_socket_ = False    # 是否加密套接字
        self.gate_ip = ""               # 网关IP地址
        self.gate_port = 0              # 网关端口
        self.connect_login_suc = False  # 连接登录是否成功
        self.reconnecting = False       # 是否正在重新连接
        self.login_suc = False          # 登录是否成功
        self.user_id = "0"              # 用户ID
        self.client_random = 0          # 客户端随机数
        self.server_random = ""         # 服务器随机数
        self.session_ticket = ""        # 会话票据
        self.session_key = ""           # 会话密钥
        self.login_token = ""           # 登录令牌
        self.login_type = LoginType.STEAMID  # 登录类型
        self.login_ErrCode = 0          # 登录错误代码
        self.error_text = ""            # 错误文本
        self.ban_type = 0               # 封禁类型
        self.ban_expire_time = 0        # 封禁到期时间
        self.notify_win = None          # 通知窗口
        self.server_time = ""           # 服务器时间
        self.recv_data_time = 0         # 接收数据时间
        self.recv_keepalive_res_time = 0  # 接收保活响应时间
        self.kick_info = {"by": "login", "reason": 0}  # 踢出信息
        
    def data_init(self):
        """重置所有登录相关属性为默认值"""
        self.encrypt_socket_ = False
        self.connect_login_suc = False
        self.reconnecting = False
        self.login_suc = False
        self.gate_ip = ""
        self.gate_port = 0
        self.user_id = ""
        self.server_random = ""
        self.session_ticket = ""
        self.session_key = ""
        self.login_ErrCode = 0
        self.error_text = ""
        self.ban_type = 0
        self.ban_expire_time = 0
        self.ban_source = None          # 此属性出现在JS重置中，但不在初始属性中
        self.server_time = ""
        self.recv_data_time = 0
        self.recv_keepalive_res_time = 0
        self.kick_info = {"by": "login", "reason": 0}