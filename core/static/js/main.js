function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
};

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

$(function() {
  var deleteVaga = function () {
      var btn = $(this);
      $.ajax({
        type: "DELETE",
        url: btn.attr("data-url"),
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        },
        success: function(data) {
          $("#table-vagas tbody").html(data.html_vagas);
        }
     });
   };

   var createCandidatura = function () {
       var btn = $(this);
       $.ajax({
         type: "GET",
         url: btn.attr("data-url"),
         beforeSend: function(xhr, settings) {
           if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
             xhr.setRequestHeader("X-CSRFToken", csrftoken);
           }
         },
         success: function(data) {
           $("#response").text(data.response);
         }
      });
    };

   $("#table-vagas").on("click", ".btn-delete-vaga", deleteVaga);
   $("#table-vagas").on("click", ".btn-new-candidatura", createCandidatura);
})
