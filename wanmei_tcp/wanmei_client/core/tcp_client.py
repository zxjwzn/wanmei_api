# wanmei_client/core/tcp_client.py
import socket
import threading
from ..protocol.message import LoginInfo
from ..utils.crypto import CryptoUtils
class TCPClient:
    def __init__(self, login_info):
        self.login_info = LoginInfo()
        self.socket = None
        self.buffer = bytearray(1048576)
        self.buffer_size = 0
        self.keepalive_timer = None
        
    def connect_login_server(self, server, port, token, user_id, login_type):
        """连接登录服务器并开始登录流程"""
        self.login_info.login_token = token
        self.login_info.user_id = user_id
        self.login_info.login_type = login_type
        
        # 创建socket连接
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        
        # 启动接收线程
        threading.Thread(target=self._receive_login_data, daemon=True).start()
        
    def connect_gate_server(self):
        """连接Gate服务器"""
        if not self.login_info.gate_ip or not self.login_info.gate_port:
            raise Exception("未获取到Gate服务器信息")
            
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.login_info.gate_ip, self.login_info.gate_port))
        
        # 启动接收线程
        threading.Thread(target=self._receive_gate_data, daemon=True).start()
    
    def send_message(self, header_bytes, body_bytes):
        """发送消息到服务器"""
        if self.login_info.encrypt_socket_:
            # 加密后发送
            encrypted_data = CryptoUtils.PVPEncrypt(body_bytes, self.login_info.session_key)
            if self.socket:
                self.socket.sendall(header_bytes + encrypted_data)
        else:
            # 直接发送
            if self.socket:
                self.socket.sendall(header_bytes + body_bytes)
    def _receive_login_data(self):
        """接收并处理登录服务器数据"""
        # 类似JS中的接收处理逻辑
        
    def _receive_gate_data(self):
        """接收并处理Gate服务器数据"""
        # 类似JS中的接收处理逻辑
        
    def start_keepalive(self):
        """启动保活定时器"""
        self.keepalive_timer = threading.Timer(10, self._send_keepalive)
        self.keepalive_timer.daemon = True
        self.keepalive_timer.start()
        
    def _send_keepalive(self):
        """发送保活消息"""
        # 构造并发送保活消息