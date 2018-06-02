
    var fileCatcher = document.getElementById('file-catcher');
    var fileInput = document.getElementById('file-input');
    var fileListDisplay = document.getElementById('file-list-display');

  var fileList = [];
  var renderFileList, sendFile;

  fileCatcher.addEventListener('submit', function (evnt) {
    evnt.preventDefault();
    fileList.forEach(function (file) {
        sendFile(file);
    });
  });

  fileInput.addEventListener('change', function (evnt) {
        fileList = [];
    for (var i = 0; i < fileInput.files.length; i++) {
        fileList.push(fileInput.files[i]);
    }
    renderFileList();
  });

  renderFileList = function () {
    fileListDisplay.innerHTML = '';
    fileList.forEach(function (file, index) {
        var fileDisplayEl = document.createElement('p');
      fileDisplayEl.innerHTML = (index + 1) + ': ' + file.name;
      fileListDisplay.appendChild(fileDisplayEl);
    });
  };

  sendFile = function (file) {
    var formData = new FormData();
    const a = {"qwe":"sad"};
    // var request = new XMLHttpRequest();

    const url = "http://127.0.0.1:8000/photo_list/";
    formData.set('file', file);
    // request.open("POST", url);

    // upload(file, url);
    // request.send(formData);
      console.log('in send');
      addNewPhoto(a);
  };




  const upload = (file, url) => {

      fetch(url, { // Your POST endpoint
        method: 'POST',
        headers: {
          "Content-Type": "multipart/form-data"
        },
        body: file // This is your file object
      }).then(
        response => response.json() // if the response is a JSON object
      ).then(
        success => console.log(success) // Handle the success response object
      ).catch(
        error => console.log(error) // Handle the error response object
      );
};


  var csrftoken = Cookies.get('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr)
    {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});




const csrfSafeMethod = (method) => {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

const beforeSend1 = (xhr, settings) => {
    let csrftoken = Cookies.get('csrftoken');
    console.log('csrftoken', csrftoken);
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        console.log(xhr);
        console.log('xhr.getResponseHeader()', xhr.getResponseHeader());
    }
};

const addNewPhoto = (dataToSend) => {



    const url = "http://127.0.0.1:8000/photo_list/";
    $.ajax({


        processData: false,

        type: "POST",
        url: url,

        data: dataToSend,

        success: function (data) {
            console.log('data', data);
        },

        error: function (data) {
            console.log('data', data);
        },
    })
};







