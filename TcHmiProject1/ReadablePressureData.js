// Keep these lines for a best effort IntelliSense of Visual Studio 2017 and higher.
/// <reference path="./../Packages/Beckhoff.TwinCAT.HMI.Framework.12.760.59/runtimes/native1.12-tchmi/TcHmi.d.ts" />

(function (/** @type {globalThis.TcHmi} */ TcHmi) {
    var Functions;
    (function (/** @type {globalThis.TcHmi.Functions} */ Functions) {
        var TcHmiProject1;
        (function (TcHmiProject1) {
            function ReadablePressureData(setpointPressure, currentPressure) {
                var diff = currentPressure - setpointPressure;
                return `Target: ${setpointPressure}\nDiff: ${diff.toFixed(3)}`;
            }
            TcHmiProject1.ReadablePressureData = ReadablePressureData;
        })(TcHmiProject1 = Functions.TcHmiProject1 || (Functions.TcHmiProject1 = {}));
    })(Functions = TcHmi.Functions || (TcHmi.Functions = {}));
})(TcHmi);
TcHmi.Functions.registerFunctionEx('ReadablePressureData', 'TcHmi.Functions.TcHmiProject1', TcHmi.Functions.TcHmiProject1.ReadablePressureData);
