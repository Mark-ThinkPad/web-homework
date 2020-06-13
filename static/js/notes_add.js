document.addEventListener('DOMContentLoaded', function () {
  $id('notes_add').addEventListener('click', function () {
    let $title = $id('title').value;
    let $content = $id('content').value;
    if ($title.length === 0 || $content.length === 0) {
      alert('请输入完整的标题和内容');
    } else {
      ajax({
        url: '/api/notes/add',
        type: 'POST',
        dataType: 'json',
        data: {
          title: $title,
          content: $content
        },
        success: function (response) {
          if (response.success) {
            window.location.href = '/notes';
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