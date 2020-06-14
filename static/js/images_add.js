document.addEventListener('DOMContentLoaded', function () {
  $id('images').addEventListener('change', function () {
    if ($id('images').value) {
      $id('images_add').disabled = false;
      $id('images_reset').disabled = false;
    } else {
      $id('images_add').disabled = true;
      $id('images_reset').disabled = true;
    }
    $id('images-preview').innerHTML = '';

    let preview = $one('#images-preview');
    let files   = $one('input[type=file]').files;

    function readAndPreview(file) {
      // 确保 `file.name` 符合我们要求的扩展名
      if ( /\.(jpe?g|png|gif)$/i.test(file.name) ) {
        let reader = new FileReader();
        reader.addEventListener("load", function () {
          let image = new Image();
          image.title = file.name;
          image.src = this.result;
          preview.appendChild(image);
        }, false);
        reader.readAsDataURL(file);
      } else {
        alert('支持的图片格式：jpg, jpeg, png, gif');
        window.location.reload();
      }
    }

    if (files) {
      [].forEach.call(files, readAndPreview);
    }
  });
  $id('images_reset').addEventListener('click', function () {
    $id('images-preview').innerHTML = '';
  });
  $id('images_add').addEventListener('click', function () {
    let files = $one('input[type=file]').files;
    let form_data = new FormData();

    for (let i = 0; i < files.length; i++) {
      form_data.append("images", files[i]);
    }
    ajax({
      url: '/api/images/add',
      type: 'POST',
      dataType: 'json',
      data: form_data,
      hasFile: true,
      success: function (response) {
        if (response.success) {
          window.location.href = '/images';
        } else {
          alert(response.message);
        }
      },
      fail: function (status) {
        alert('HTTP状态码: ' + status);
      }
    });
  });
});