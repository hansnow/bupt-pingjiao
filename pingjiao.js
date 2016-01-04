// 评语，urlencode(s.encode('gbk'))
var comment = '%BD%B2%BF%CE%C8%CF%D5%E6';
// task_array里包含了所有待评课程的信息
var task_array = new Array();
var el_array = window.frames['bottomFrame'].frames['mainFrame'].document.querySelectorAll('[title=评估]');
for (var i = el_array.length - 1; i >= 0; i--) {
    info = el_array[i].getAttribute('name').split('#@');
    var task = {
        wjbm: info[0],
        bpr: info[1],
        pgnr: info[5],
        wjmc: info[3],
        bprm: info[2],
        pgnrm: info[4]
    };
    task_array.push(task);
};

// 手动发xhr
var xmlhttp;
var task;
// stop变量用来控制xhr的发送数量，以防连续不断的发送请求，不知道有没有更优雅的解决方案
var stop = task_array.length * 2;
if( window.XMLHttpRequest ){
    xmlhttp = new XMLHttpRequest();
}else{
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.onreadystatechange = function(){
    if( xmlhttp.readyState == 4 && xmlhttp.status == 200 ){
        if( stop !== 0 ){
            if ( stop%2 === 0 ){
                // 预备post
                task = task_array.pop()
                xmlhttp.open("POST","jxpgXsAction.do",true);
                xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
                xmlhttp.send("wjbm="+ task.wjbm +"&bpr="+ task.bpr +"&pgnr="+ task.pgnr +"&oper=wjShow&wjmc="+ task.wjmc +"&bprm="+ task.bprm +"&pgnrm="+ task.pgnrm +"&pageSize=20&page=1&currentPage=1&pageNo=");

            }else{
                // 评教post
                xmlhttp.open("POST","jxpgXsAction.do?oper=wjpg",true);
                xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
                xmlhttp.send("wjbm="+ task.wjbm +"&bpr="+ task.bpr +"&pgnr="+ task.pgnr +"&0000000021=10_0.95&0000000022=10_0.95&0000000023=5_0.95&0000000024=20_0.95&0000000025=10_0.95&0000000026=5_0.95&0000000027=5_0.95&0000000028=20_0.95&0000000029=10_0.95&0000000030=5_0.95&zgpj="+comment);

            }
            stop--;
        }else{
            alert('已完成，请刷新页面查看效果');
        }
    }
}
// 这个一个没用的请求，用来使`stop`的逻辑更简单
xmlhttp.open("GET","jxpgXsAction.do?oper=listWj",true);
xmlhttp.send();