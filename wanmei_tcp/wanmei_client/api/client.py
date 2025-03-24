from ..protocol.message import MessageHeader
from ..protocol.constants import LaaderProtocol
from ..utils.binary import Serializer
from .reqs import Reqs
class WanmeiClient:
    class LadderAPI:
        @staticmethod
        def enterTeam(params):
            # 创建消息头
            header = MessageHeader()
            header.type = LaaderProtocol.MessageType.MT_ENTER_TEAM_REQ
            header.source = 123456
            header.attach_id1 = LaaderProtocol.GameType.CSGO

            # 创建请求对象
            req = Reqs.EnterTeamReq(params)
            req.match_mode = LaaderProtocol.CSGOMatchMode.MATCH_MODE_RANK_MATCH

            # 序列化请求对象
            binary_data = Serializer.serializeBinary(req)

            # 设置消息总长度
            total_length = MessageHeader.HEAD_SIZE + len(binary_data)
            header.length = total_length

            header_bytes = header.serialize()
            print(header_bytes)
            print(binary_data)
            #LoginSession.send_message(header_bytes, binary_data)