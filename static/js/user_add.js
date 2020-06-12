document.addEventListener('DOMContentLoaded', function () {
  $id('user_add').addEventListener('click', function () {
    let $username = $id('username').value;
    let $password = $id('password').value;
    if ($username.length === 0 || $password.length === 0) {
      alert('请输入完整的用户名和密码');
    } else {
      ajax({
        url: '/api/user/add',
        type: 'POST',
        dataType: 'json',
        data: {
          username: $username,
          password: $password
        },
        success: function (response) {
          alert(response.message);
          if (response.success) {
            window.location.href = '/';
          }
        },
        fail: function (status) {
          alert('HTTP状态码: ' + status);
        }
      });
    }
  });
});