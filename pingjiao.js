// ���urlencode(s.encode('gbk'))
var comment = '%BD%B2%BF%CE%C8%CF%D5%E6';
// task_array����������д����γ̵���Ϣ
var task_array = new Array();
var el_array = window.frames['bottomFrame'].frames['mainFrame'].document.querySelectorAll('[title=����]');
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

// �ֶ���xhr
var xmlhttp;
var task;
// stop������������xhr�ķ����������Է��������ϵķ������󣬲�֪����û�и����ŵĽ������
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
                // Ԥ��post
                task = task_array.pop()
                xmlhttp.open("POST","jxpgXsAction.do",true);
                xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
                xmlhttp.send("wjbm="+ task.wjbm +"&bpr="+ task.bpr +"&pgnr="+ task.pgnr +"&oper=wjShow&wjmc="+ task.wjmc +"&bprm="+ task.bprm +"&pgnrm="+ task.pgnrm +"&pageSize=20&page=1&currentPage=1&pageNo=");

            }else{
                // ����post
                xmlhttp.open("POST","jxpgXsAction.do?oper=wjpg",true);
                xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
                xmlhttp.send("wjbm="+ task.wjbm +"&bpr="+ task.bpr +"&pgnr="+ task.pgnr +"&0000000021=10_0.95&0000000022=10_0.95&0000000023=5_0.95&0000000024=20_0.95&0000000025=10_0.95&0000000026=5_0.95&0000000027=5_0.95&0000000028=20_0.95&0000000029=10_0.95&0000000030=5_0.95&zgpj="+comment);

            }
            stop--;
        }else{
            alert('����ɣ���ˢ��ҳ��鿴Ч��');
        }
    }
}
// ���һ��û�õ���������ʹ`stop`���߼�����
xmlhttp.open("GET","jxpgXsAction.do?oper=listWj",true);
xmlhttp.send();