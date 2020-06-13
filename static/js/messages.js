document.addEventListener('DOMContentLoaded', function () {
  // 将UTC时区转化为本地时区
  setLocalTime();
  // 发送留言
  $id('messages_add').addEventListener('click', function () {
    let $content = $id('mContent').value;
    if ($content.length === 0) {
      alert('请输入留言');
    } else {
      ajax({
        url: '/api/messages/add',
        type: 'POST',
        dataType: 'json',
        data: {
          content: $content
        },
        success: function (response) {
          if (response.success) {
            window.location.reload();
          } else {
            alert(response.message);
          }
        },
        fail: function (status) {
          alert('HTTP状态码: ' + status);
        }
      });
    }
  });
});