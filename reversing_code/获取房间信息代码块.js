//函数实际实现
function (e, t, r) {
  "use strict";
  const i = global.logger.matchMgr,
    s = r(10),
    a = r(11),
    n = r(8),
    o = r(52),
    u = r(20),
    p = r(25),
    c = r(34),
    m = "CSGO_LADDER_API: ";
  e.exports = class {
    static enterTeam(e) {
      i.trace(`${m}call - enterTeam, params: ${JSON.stringify(e)}`);
      let t = new a();
      (t.type = o.MessageType.MT_ENTER_TEAM_REQ),//位于项目中的wanmei_tcp/wanmei_client/protocol/constants.py中RoomProtocol类下的MessageType.MT_ENTER_TEAM_REQ
        (t.source = u.user_id()),//实际上就是用户的steam64id,在项目中的wanmei_tcp/wanmei_client/protocol/message.py中LoginInfo类有定义user_id
        (t.attach_id1 = n.GameType.CSGO);//位于项目中的wanmei_tcp/wanmei_client/protocol/constants.py中RoomProtocol类下的GameType.CSGO
      let r = new o.EnterTeamReq(e);//项目中的reversing_code/enterTeam序列化相关.js中有定义
      r.match_mode = o.CSGOMatchMode.MATCH_MODE_RANK_MATCH;//位于项目中的wanmei_tcp/wanmei_client/protocol/constants.py中RoomProtocol类下的CSGOMatchMode.MATCH_MODE_RANK_MATCH
      let p = s.serializeBinary(r),//位于项目中的reversing_code/enterTeam序列化相关.js中
        c = a.head_size + p.length;//a.head_size即项目中的wanmei_tcp/wanmei_client/protocol/message.py中Message类下的head_size，被设定为常量48
      t.length = c;
      let l = t.serialize();//位于项目中的wanmei_tcp/wanmei_client/protocol/message.py中Message类下的serialize方法
      u.send_message(l, p);//项目中的reversing_code/gate tcp服务器连接相关.js中
    }
//ipc通信部分
function (e, t, r) {
  "use strict";
  const { ipcMain: i } = r(2),
    s = global.logger.matchMgr,
    a = r(12),
    n = r(87),
    o = r(114),
    u = r(10),
    p = r(11),
    c = r(52),
    m = r(2714),
    l = r(2715),
    d = r(26),
    y = r(84),
    h = (r(29), r(8), r(23)),
    _ = r(25),
    g = r(14),
    S = r(32);
  r(109), r(188), r(13);
  let b = null,
    T = !1;
  const f = "CSGO_LADDER: ";
  e.exports = class {
    static ipcListen() {
      1 != T &&
        ((T = !0),
        i.on(m.ReqType.MT_ENTER_TEAM_REQ, (e, t) => {
          s.trace(${f}enter Team, team info: ${JSON.stringify(t)}),
            l.enterTeam(t);
        })

//调用函数的代码
const a = e.inputValue.replace("0", ""),
s = yield v["default"].send(
R.a.ReqType.MT_ENTER_TEAM_REQ,
{ team_id: a },
R.a.ResType.MT_ENTER_TEAM_RES,
);