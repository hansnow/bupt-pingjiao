if (window.document.title == "URP 综合教务系统 - 教学评估 - 教学评估") {
    x = window.frames[1].frames[2].document.getElementsByTagName("input");
}else if (window.document.title == "问卷评估页面"){
    x = window.document.getElementsByTagName("input");
}else{
    alert("请确认一个你现在是不是处于正确的页面上，本程序只能在教学评估页面运行！")
}
data = new Array();
for(var i=0;i<x.length;i++){if(x[i].type=="hidden"){data.push(x[i].value)}};
function post(path, params, method) {
method = method || "post"; // Set method to post by default if not specified.

// The rest of this code assumes you are not using a library.
// It can be made less wordy if you use one.
var form = document.createElement("form");
form.setAttribute("method", method);
form.setAttribute("action", path);

for(var key in params) {
    if(params.hasOwnProperty(key)) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
     }
}

document.body.appendChild(form);
form.submit();
}
post('http://10.3.240.72/jxpgXsAction.do?oper=wjpg', {
    'wjbm':data[0],
    'bpr':data[1],
    'pgnr':data[2],
    '0000000021':'10_0.95',
    '0000000022':'10_0.95',
    '0000000023':'5_0.95',
    '0000000024':'20_0.95',
    '0000000025':'10_0.95',
    '0000000026':'5_0.95',
    '0000000027':'5_0.95',
    '0000000028':'20_0.95',
    '0000000029':'10_0.95',
    '0000000030':'5_0.95',
    'zgpj':'老师讲课很认真的啦~'
},"post");
