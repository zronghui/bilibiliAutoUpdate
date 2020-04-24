let gotFile = function (name, content) {
  let danmaku = parseFile(content);
  let ass = generateASS(setPosition(danmaku), {
    'title': document.title,
    'ori': name,
  });
  startDownload('\ufeff' + ass, name.replace(/\.[^.]*$/, '') + '.ass');
};
window.addEventListener('load', function () {
  let upload = document.querySelector('#upload');
  upload.addEventListener('change', function () {
    console.info('upload.files', upload.files)
    let readers = []
    for (let i = 0; i < upload.files.length; i++) {
      readers.push(new FileReader())
    }
    for (let i = 0; i < upload.files.length; i++){
      let file = upload.files[i]
      let reader = readers[i];
      console.info('file:', file)
      let name = file.name;
      if (file.size > (1 << 24)) error();
      else reader.addEventListener('load', function () {
        gotFile(name, reader.result);
      });
      reader.readAsText(file);
    }
    upload.value = '';
  });
});


if (navigator.userAgent.match(/^Mozilla\/5.0 \([^)]+; rv:[\d.]+\) Gecko\/[\d]{8} Firefox\/[\d.]+$/)) {
  const style = document.createElement('style');
  style.innerHTML = '.addon { display: block; }';
  document.documentElement.appendChild(style);
}
