function (e, t, r) {
  var i = r(19),
    s = (e.exports = {}),
    a = Math.pow(2, 24),
    n = Math.pow(2, 31),
    o = Math.pow(2, 32),
    u = Math.pow(10, 11);
  (s.toDecimalString = function (e) {
    var t = e.buffer,
      r = e.offset;
    if ((t[r] || 224 & t[r + 1]) && (~t[r] || ~(224 & t[r + 1]))) {
      var i = 128 & t[r];
      if (i) {
        for (var s = !1, n = new Buffer(8), p = 7; p >= 0; --p)
          (n[p] = (~t[r + p] + (s ? 0 : 1)) & 255), (s |= t[r + p]);
        t = n;
      }
      var c = t[r + 1] + (t[r] << 8),
        m =
          t[r + 7] +
          (t[r + 6] << 8) +
          (t[r + 5] << 16) +
          t[r + 4] * a +
          (t[r + 3] + (t[r + 2] << 8)) * o +
          74976710656 * c,
        l = Math.floor(m / u) + 2814 * c;
      return (
        (m = ("00000000000" + String(m % u)).slice(-11)),
        (i ? "-" : "") + String(l) + m
      );
    }
    return e.toString();
  }),
    (s.fromDecimalString = function (e) {
      var t = "-" === e.charAt(0);
      if (e.length < (t ? 17 : 16)) return new i(+e);
      if (e.length > (t ? 20 : 19))
        throw new RangeError("Too many digits for Int64: " + e);
      var r = +e.slice(t ? 1 : 0, -15),
        s = +e.slice(-15) + 2764472320 * r,
        a = Math.floor(s / o) + 232830 * r;
      if (((s %= o), a >= n && (!t || a != n || 0 != s)))
        throw new RangeError("The magnitude is too large for Int64.");
      return (
        t &&
          ((a = ~a),
          0 === s ? (a = (a + 1) & 4294967295) : (s = 1 + ~s),
          (a |= 2147483648)),
        new i(a, s)
      );
    });
},这个是toDecimalString和fromDecimalString的js代码
function u(e, t, r) { //通过toString获取到的TBinaryProtocol 实现 
  (this.trans = e),
    (this.strictRead = void 0 !== t && t),
    (this.strictWrite = void 0 === r || r),
    (this._seqid = null);
}
function a(e, t) {// 通过toString获取到的TFramedTransport 实现 
  (this.inBuf = e || new Buffer(0)),
    (this.outBuffers = []),
    (this.outCount = 0),
    (this.readPos = 0),
    (this.onFlush = t);
}
function a(e, t) {//  通过toString获取到的TBufferedTransport  实现 
  (this.defaultReadBufferSize = 1024),
    (this.writeBufferSize = 512),
    (this.inBuf = new Buffer(this.defaultReadBufferSize)),
    (this.readCursor = 0),
    (this.writeCursor = 0),
    (this.outBuffers = []),
    (this.outCount = 0),
    (this.onFlush = t);
}
function (e, t, r) {//
  var i = r(27);
  r(174);
  var s = r(19),
    a = r(813);
  class n extends i.TBinaryProtocol {
    constructor(e, t, r) {
      super(e, t, r);
    }
    readI64() {
      return a.toDecimalString(super.readI64());
    }
    writeI64(e) {
      return super.writeI64(a.fromDecimalString(e));
    }
  }
  e.exports = class {
    static serializeBinary(e) {//serializeBinary函数
      let t;
      const r = new i.TBufferedTransport(null, function (e) {
          t = e;
        }),
        s = new n(r);
      return e.write(s), s.flush(), t;
    }
    static deserializeBinary(e, t) {//deserializeBinary函数
      const r = new i.TFramedTransport(e),
        s = new n(r),
        a = new t();
      return a.read(s), a;
    }
  };
},
var P = (e.exports.EnterTeamReq = function (e) {//EnterTeamReq(e)的构造函数
  (this.team_id = null),
    (this.match_mode = null),
    (this.enter_channel = null),
    (this.grudge_team_id = null),
    e &&
      (void 0 !== e.team_id &&
        null !== e.team_id &&
        (this.team_id = e.team_id),
      void 0 !== e.match_mode &&
        null !== e.match_mode &&
        (this.match_mode = e.match_mode),
      void 0 !== e.enter_channel &&
        null !== e.enter_channel &&
        (this.enter_channel = e.enter_channel),
      void 0 !== e.grudge_team_id &&
        null !== e.grudge_team_id &&
        (this.grudge_team_id = e.grudge_team_id));
});
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
      (t.type = o.MessageType.MT_ENTER_TEAM_REQ),//实际值为9004
        (t.source = u.user_id()),//示例值为1641013516
        (t.attach_id1 = n.GameType.CSGO);//实际值为8
      let r = new o.EnterTeamReq(e);//定义见上方代码块
      r.match_mode = o.CSGOMatchMode.MATCH_MODE_RANK_MATCH;//实际值为1
      let p = s.serializeBinary(r),//定义见上方代码块
        c = a.head_size + p.length;//a.head_size为常量48
      t.length = c;
      let l = t.serialize();//暂时不管
      u.send_message(l, p);//发送相关数据，暂时不管
    }