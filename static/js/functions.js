// 元素选择器
function $id(id){return id?document.getElementById(id):document.body}
function $one(dom){return dom?document.querySelector(dom):document.body}
function $all(dom){return dom?document.querySelectorAll(dom):document.body}

/**
 * @typedef {Object} options
 * @property {string} url
 * @property {string} type
 * @property {string} dataType
 * @property {Object | FormData} data
 * @property {boolean} hasFile
 * @property {function(response: Object): void} success
 * @property {function(status: number): void} fail
 */
/**
 * 自定义Ajax函数
 * @param {Object} options
 */
function ajax(options) {
  options = options || {};
  options.type = (options.type || "GET").toUpperCase();
  options.dataType = options.dataType || "json"; // 服务器返回的数据类型
  options.hasFile = options.hasFile || false; // 是否上传文件
  // 处理传入的数据
  let params;
  if (options.hasFile) {
    // 有文件时传入的是FormData, 无需处理
    params = options.data
  } else {
    // 没有文件时对传入的参数格式化
    params = formatParams(options.data);
  }
  // 创建 - 非IE6 - 第一步
  let xhr;
  if (window.XMLHttpRequest) {
    xhr = new XMLHttpRequest();
  } else { //IE6及其以下版本浏览器
    xhr = new ActiveXObject('Microsoft.XMLHTTP');
  }
  // 接收 - 第三步
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      let status = xhr.status;
      if (status === 200) {
        let response = JSON.parse(xhr.responseText)
        options.success && options.success(response);
      } else {
        options.fail && options.fail(status);
      }
    }
  }
  // 连接 和 发送 - 第二步
  if (options.type === "GET") {
    xhr.open("GET", options.url + "?" + params, true);
    xhr.send(null);
  } else if (options.type === "POST") {
    xhr.open("POST", options.url, true);
    if (!options.hasFile) {
      // 不上传文件时, 设置表单提交时的内容类型
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    }
    xhr.send(params);
  }
}
// 格式化参数
function formatParams(data) {
  let arr = [];
  for (let name in data) {
    arr.push(encodeURIComponent(name) + "=" + encodeURIComponent(data[name]));
  }
  return arr.join("&");
}
// 数据库默认使用UTC时区, 而我们所在的时区是UTC+8
// 所以直接从数据库取出的时间比本地时间慢8小时
// 可以在前端把UTC时间转化为本地时间
function setLocalTime() {
  let all = $all('.datetime');
  all.forEach(function (item) {
    let time = item.innerText;
    time = new Date(time + ' GMT')
    item.innerText = time.toLocaleString()
  });
}
