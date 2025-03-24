from thrift.Thrift import TType
class Reqs:
    class EnterTeamReq:
        def __init__(self, params=None):
            self.team_id = None
            self.match_mode = None
            self.enter_channel = None
            self.grudge_team_id = None
            
            if params:
                if 'team_id' in params and params['team_id'] is not None:
                    self.team_id = params['team_id']
                if 'match_mode' in params and params['match_mode'] is not None:
                    self.match_mode = params['match_mode']
                if 'enter_channel' in params and params['enter_channel'] is not None:
                    self.enter_channel = params['enter_channel']
                if 'grudge_team_id' in params and params['grudge_team_id'] is not None:
                    self.grudge_team_id = params['grudge_team_id']
        
        def write(self, protocol):
            if self.team_id is not None:
                protocol.writeFieldBegin('team_id', TType.I64, 1)
                protocol.writeI64(str(self.team_id))
                protocol.writeFieldEnd()
            
            if self.match_mode is not None:
                protocol.writeFieldBegin('match_mode', TType.I32, 2)
                protocol.writeI32(self.match_mode)
                protocol.writeFieldEnd()
            
            if self.enter_channel is not None:
                protocol.writeFieldBegin('enter_channel', TType.I32, 3)
                protocol.writeI32(self.enter_channel)
                protocol.writeFieldEnd()
            
            if self.grudge_team_id is not None:
                protocol.writeFieldBegin('grudge_team_id', TType.I64, 4)
                protocol.writeI64(str(self.grudge_team_id))
                protocol.writeFieldEnd()
            
            protocol.writeFieldStop()
        
        def read(self, protocol):
            while True:
                field_type, field_id = protocol.readFieldBegin()
                if field_type == TType.STOP:
                    break
                    
                if field_id == 1:
                    if field_type == TType.I64:
                        self.team_id = protocol.readI64()
                elif field_id == 2:
                    if field_type == TType.I32:
                        self.match_mode = protocol.readI32()
                elif field_id == 3:
                    if field_type == TType.I32:
                        self.enter_channel = protocol.readI32()
                elif field_id == 4:
                    if field_type == TType.I64:
                        self.grudge_team_id = protocol.readI64()
                
                protocol.readFieldEnd()