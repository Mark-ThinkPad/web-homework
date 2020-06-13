document.addEventListener('DOMContentLoaded', function () {
  // 数据库默认使用UTC时区, 而我们所在的时区是UTC+8
  // 所以直接从数据库取出的时间比本地时间慢8小时
  // 可以在前端把UTC时间转化为本地时间
  let time = $id('time').innerText;
  time = new Date(time + ' GMT')
  console.log(time.toLocaleString())
});