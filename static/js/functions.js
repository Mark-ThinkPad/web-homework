// 元素选择器
function $id(id){return id?document.getElementById(id):document.body}
function $one(dom){return dom?document.querySelector(dom):document.body}
function $all(dom){return dom?document.querySelectorAll(dom):document.body}
// 自定义Ajax函数
let f1=String.fromCharCode(198);
let f2=String.fromCharCode(199);
function ajax(url, send, postback, f, moth)
{
  if(!url)return;
  moth=moth?"GET":"POST";
  let ajx=new XMLHttpRequest();
  ajx.open(moth,url,!f);
  ajx.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
  if(postback)ajx.onreadystatechange=function(){if(ajx.readyState==4&&ajx.status==200)postback(ajx.responseText)};
  ajx.send(send)
}