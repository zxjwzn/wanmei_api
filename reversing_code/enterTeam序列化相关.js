r(19) 实现 function (e, t) {
  e instanceof Buffer
    ? ((this.buffer = e), (this.offset = t || 0))
    : "[object Uint8Array]" == Object.prototype.toString.call(e)
      ? ((this.buffer = new Buffer(e)), (this.offset = t || 0))
      : ((this.buffer = this.buffer || new Buffer(8)),
        (this.offset = 0),
        this.setValue.apply(this, arguments));
}
r(27) TBinaryProtocol 实现 function u(e, t, r) { 
  (this.trans = e),
    (this.strictRead = void 0 !== t && t),
    (this.strictWrite = void 0 === r || r),
    (this._seqid = null);
}
r(27) TFramedTransport 实现 function a(e, t) {
  (this.inBuf = e || new Buffer(0)),
    (this.outBuffers = []),
    (this.outCount = 0),
    (this.readPos = 0),
    (this.onFlush = t);
}
r(27) TBufferedTransport  实现 function a(e, t) {
  (this.defaultReadBufferSize = 1024),
    (this.writeBufferSize = 512),
    (this.inBuf = new Buffer(this.defaultReadBufferSize)),
    (this.readCursor = 0),
    (this.writeCursor = 0),
    (this.outBuffers = []),
    (this.outCount = 0),
    (this.onFlush = t);

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
},
function (e, t, r) {
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
        static Bytes2HexString(e) {
          let t = "";
          for (let r = 0; r < e.length; r++) {
            let i = e[r].toString(16);
            1 === i.length && (i = "0" + i), (t += i.toUpperCase());
          }
          return t;
        }
        static Hexstring2btye(e) {
          let t = 0,
            r = e.length;
          if (r % 2 != 0) return null;
          r /= 2;
          let i = new Array();
          for (let s = 0; s < r; s++) {
            let r = e.substr(t, 2),
              s = parseInt(r, 16);
            i.push(s), (t += 2);
          }
          return i;
        }
        static writeUInt64BE(e, t, r) {
          return (
            void 0 === r ||
              0 === r ||
              "" === r ||
              a.fromDecimalString(r).toBuffer().copy(e, t),
            e
          );
        }
        static readUInt64BE(e, t) {
          var r = new s(e, t);
          return a.toDecimalString(r);
        }
        static serializeBinary(e) {
          let t;
          const r = new i.TBufferedTransport(null, function (e) {
              t = e;
            }),
            s = new n(r);
          return e.write(s), s.flush(), t;
        }
        static deserializeBinary(e, t) {
          const r = new i.TFramedTransport(e),
            s = new n(r),
            a = new t();
          return a.read(s), a;
        }
      };
    },请你看下这段js代码，我想让你根据这个写一个python实现，写出与js功能完全一致的Bytes2HexString Hexstring2btye writeUInt64BE readUInt64BE serializeBinary deserializeBinary函数如果代码提供的内容不完整，比如有些变量或者函数的定义没提供的，请你指出，我会告诉你

    