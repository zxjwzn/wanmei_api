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
      console.warn("MT_ENTER_TEAM_REQ",o.MessageType.MT_ENTER_TEAM_REQ);
      console.warn("GameType.CSGO:",n.GameType.CSGO);
      console.warn("MATCH_MODE_RANK_MATCH",o.CSGOMatchMode.MATCH_MODE_RANK_MATCH);
      (t.type = o.MessageType.MT_ENTER_TEAM_REQ),
        (t.source = u.user_id()),
        (t.attach_id1 = n.GameType.CSGO);
      let r = new o.EnterTeamReq(e);
      r.match_mode = o.CSGOMatchMode.MATCH_MODE_RANK_MATCH;
      let p = s.serializeBinary(r),
        c = a.head_size + p.length;
      t.length = c;
      let l = t.serialize();
      u.send_message(l, p);
    }
//前置代码
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

//调用代码
const a = e.inputValue.replace("0", ""),
s = yield v["default"].send(
R.a.ReqType.MT_ENTER_TEAM_REQ,
{ team_id: a },
R.a.ResType.MT_ENTER_TEAM_RES,
);
fs.appendFileSync("C:\\wm.log", `MT_ENTER_TEAM_RES result: ${JSON.stringify(s)}\n`);