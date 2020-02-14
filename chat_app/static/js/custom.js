$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});
name_flag = 0;
lname_flag = 0;
uname_flag = 0;
pswd_flag = 0;
cpswd_flag = 0;
phn_flag = 0;
image_flag = 0;
email_flag = 0;
var inputs_profile = document.querySelectorAll('#form2 input');
var validateForm3 = function() {
  if ( !validateInput1() ) {
    return false;
  }
  if(!validateInput2()){
    return false;
  }
  if(!validateInput3()){
    return false;
  }
  if(!validateInput4()){
    return false;
  }
  return true;
}
for ( var i = 0, len = inputs_profile.length; i < len; i++ )
{
  var checkValid1 = function() {
    console.log(validateForm3());
    document.getElementById('update_submit').disabled = !validateForm3();
  }
  inputs_profile[i].addEventListener('focusout', checkValid1);
}


function allvalidation(){
    if(name_flag && lname_flag && uname_flag && pswd_flag && cpswd_flag && phn_flag && image_flag && email_flag){
        $("#registration_form").submit();
    }
    else{
    alert("Please correct the Errors");
    }
}
function validatename() {
  var name = form.fname.value;
  if (name == ""){
    name_flag = 0;
    document.getElementById("fnameerr").innerHTML = "Please Enter First Name";
    document.getElementById("fname").style.border = "1px solid red";
  }
  else if (name.length < 3) {
    name_flag = 0;
    document.getElementById("fnameerr").innerHTML = "First Name must be greater than 3 characters";
    document.getElementById("fname").style.border = "1px solid red";
  } else {
    name_flag = 1;
    document.getElementById("fnameerr").innerHTML = "";
    document.getElementById("fname").style.border = "1px solid green";
  }
}
function validatelname() {
  var name = form.lname.value;
  if (name == ""){
    lname_flag = 0;
    document.getElementById("lnameerr").innerHTML = "Please Enter Last Name";
    document.getElementById("lname").style.border = "1px solid red";
  }
  else if (name.length < 3) {
    lname_flag = 0;
    document.getElementById("lnameerr").innerHTML = "Last Name must be greater than 3 characters";
    document.getElementById("lname").style.border = "1px solid red";
  } else {
    lname_flag = 1;
    document.getElementById("lnameerr").innerHTML = "";
    document.getElementById("lname").style.border = "1px solid green";
  }
}
function validateuname() {
  var name = form.uname.value;
  if (name == ""){
    uname_flag = 0;
    document.getElementById("unameerr").innerHTML = "Please Enter User Name";
    document.getElementById("uname").style.border = "1px solid red";
  }
  else if (name.length < 3) {
    uname_flag = 0;
    document.getElementById("unameerr").innerHTML = "User Name must be greater than 3 characters";
    document.getElementById("uname").style.border = "1px solid red";
  } else {
    uname_flag = 1;
    document.getElementById("unameerr").innerHTML = "";
    document.getElementById("uname").style.border = "1px solid green";
  }
}
function pswdvalidation() {
  var pass = form.pswd.value;
  var uppercount = 0;
  var lowercount = 0;
  var specialcount = 0;
  var digitcount = 0;
  var temp;
  for (var i = 0; i < pass.length; i++) {
    temp = pass.charCodeAt(i);
    if (temp > 47 && temp < 58) {
      digitcount += 1;
    } else if (temp > 64 && temp < 91) {
      uppercount += 1;
    } else if (temp > 96 && temp < 123) {
      lowercount += 1;
    } else if (
      (temp > 32 && temp < 48) ||
      (temp > 57 && temp < 65) ||
      (temp > 90 && temp < 97) ||
      (temp > 122 && temp < 127)
    ) {
      specialcount += 1;
    } else {
    }
  }
  if (pass == ""){
    pswd_flag = 0;
    document.getElementById("psderr").innerHTML = "Please Enter Password";
    document.getElementById("pswd").style.border = "1px solid red";
  }
  else if (pass.length < 8 || pass.length > 12) {
    pswd_flag = 0;
    document.getElementById("psderr").innerHTML =
      "Password must be between 8 to 12 characters";
    document.getElementById("pswd").style.border = "1px solid red";
  } else if (digitcount == 0) {
    pswd_flag = 0;
    document.getElementById("psderr").innerHTML = "Please enter a number";
    document.getElementById("pswd").style.border = "1px solid red";
  } else if (uppercount == 0) {
    pswd_flag = 0;
    document.getElementById("psderr").innerHTML = "Please enter a uppercase";
    document.getElementById("pswd").style.border = "1px solid red";
  } else if (lowercount == 0) {
    pswd_flag = 0;
    document.getElementById("psderr").innerHTML = "Please enter a lowercase";
    document.getElementById("pswd").style.border = "1px solid red";
  } else if (specialcount == 0) {
    pswd_flag = 0;
    document.getElementById("psderr").innerHTML =
      "Please enter a special character";
    document.getElementById("pswd").style.border = "1px solid red";
  } else {
    pswd_flag = 1;
    document.getElementById("psderr").innerHTML = "";
    document.getElementById("pswd").style.border = "1px solid green";
  }
}
function cpswdvalidation() {
  var cpsd = form.cpswd.value;
  var psd = form.pswd.value;
  if (cpsd == "") {
    cpswd_flag = 0;
    document.getElementById("cpswderr").innerHTML = "Please enter password";
    document.getElementById("cpswd").style.border = "1px solid red";
  } else if (cpsd != psd) {
    cpswd_flag = 0;
    document.getElementById("cpswderr").innerHTML = "Password mismatched";
    document.getElementById("cpswd").style.border = "1px solid red";
  } else {
    cpswd_flag = 1;
    document.getElementById("cpswderr").innerHTML = "";
    document.getElementById("cpswd").style.border = "1px solid green";
  }
}
function validatephn() {
  var phnno = form.phn.value;
  var reg = /^[6-9]\d{9}$/;
  if (phnno == ""){
    phn_flag = 0;
    document.getElementById("phnerr").innerHTML = "Please Enter Phone No.";
    document.getElementById("phone").style.border = "1px solid red";
  }
  else if (phnno.search(reg) == -1) {
    phn_flag = 0;
    document.getElementById("phnerr").innerHTML = "Enter valid mobile no.";
    document.getElementById("phone").style.border = "1px solid red";
  }
  else if (phnno.length != 10) {
    phn_flag = 0;
    document.getElementById("phnerr").innerHTML = "Enter 10 digit number only";
    document.getElementById("phone").style.border = "1px solid red";
   }
    else {
    phn_flag = 1;
    document.getElementById("phnerr").innerHTML = "";
    document.getElementById("phone").style.border = "1px solid green";
  }
}
function loadFile(){
	if(validate_single_fileupload(document.getElementById('singleFile'))){
		var reader = new FileReader();
		reader.onload = function(){
			var output = document.getElementById('img-preview');
			output.src = reader.result;
			output.style.width = '150px';
			output.style.height = '150px';
			output.style.display = 'block';
		};
		reader.readAsDataURL(event.target.files[0]);
		image_flag = 1;
	}
	else{
		image_flag = 0;
		document.getElementById('img-preview').style.display = 'none';
	}
}
function validate_single_fileupload(file){

//    console.log(file.files[0].size/1024/1024+" MB")
	var allowed_extensions = new Array("jpg","png");
	var file_extension = file.value.split('.').pop().toLowerCase();
	for(var i = 0; i <= allowed_extensions.length; i++)
	{
		if(allowed_extensions[i]==file_extension)
		{
			document.getElementById('extension').innerHTML = '';
			if(file.files[0].size/1024/1024 > 5){
				document.getElementById('extension').innerHTML = 'File size must be less than 5MB.'
				return false;
			}
			return true;
		}
	}
	file.value = '';
	document.getElementById('extension').innerHTML = 'Only .jpg and .png files are allowed.';
	return false;
}
function emailvalidation(){
	var email = document.getElementById("email").value;
    var filter = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    if(email == ""){
        email_flag = 0;
        document.getElementById("emailerr").innerHTML="Please Enter Email";
        document.getElementById('email').style.border = "1px solid red";
    }
    else if(!(email.search (filter) != -1)){
        email_flag = 0;
        document.getElementById("emailerr").innerHTML="Please Enter Valid Email";
        document.getElementById('email').style.border = "1px solid red";
    }
    else{
        email_flag = 1;
        document.getElementById("emailerr").innerHTML="";
        document.getElementById('email').style.border = "1px solid green";
    }
}

var validateInput1 = function validatename() {
  var name = form.fname.value;
  if (name == ""){
    document.getElementById("fnameerr").innerHTML = "Please Enter First Name";
    document.getElementById("fname").style.border = "1px solid red";
    return false;
  }
  else if (name.length < 3) {
    document.getElementById("fnameerr").innerHTML = "First Name must be greater than 3 characters";
    document.getElementById("fname").style.border = "1px solid red";
    return false;
  } else {
    document.getElementById("fnameerr").innerHTML = "";
    document.getElementById("fname").style.border = "1px solid green";
    return true;
  }
}
var validateInput2 = function validatelname() {
  var name = form.lname.value;
  if (name == ""){
    document.getElementById("lnameerr").innerHTML = "Please Enter Last Name";
    document.getElementById("lname").style.border = "1px solid red";
    return false;
  }
  else if (name.length < 3) {
    document.getElementById("lnameerr").innerHTML = "Last Name must be greater than 3 characters";
    document.getElementById("lname").style.border = "1px solid red";
    return false;
  } else {
    document.getElementById("lnameerr").innerHTML = "";
    document.getElementById("lname").style.border = "1px solid green";
    return true;
  }
}
var validateInput3 = function emailvalidation(){
	var email = document.getElementById("email").value;
    var filter = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    if(email == ""){
        document.getElementById("emailerr").innerHTML="Please Enter Email";
        document.getElementById('email').style.border = "1px solid red";
        return false;
    }
    else if(!(email.search (filter) != -1)){
        document.getElementById("emailerr").innerHTML="Please Enter Valid Email";
        document.getElementById('email').style.border = "1px solid red";
        return false;
    }
    else{
        document.getElementById("emailerr").innerHTML="";
        document.getElementById('email').style.border = "1px solid green";
        return true;
    }
}
var validateInput4 = function validateuname() {
  var name = form.uname.value;
  if (name == ""){
    document.getElementById("unameerr").innerHTML = "Please Enter User Name";
    document.getElementById("uname").style.border = "1px solid red";
    return false;
  }
  else if (name.length < 3) {
    document.getElementById("unameerr").innerHTML = "User Name must be greater than 3 characters";
    document.getElementById("uname").style.border = "1px solid red";
    return false;
  } else {
    document.getElementById("unameerr").innerHTML = "";
    document.getElementById("uname").style.border = "1px solid green";
    return true;
  }
}



var inputs_invite = document.querySelectorAll('#invite_form input');
console.log(inputs_invite)
var validateForm2 = function() {
  if ( !validateInvite() ) {
    return false;
  }
  return true;
}

var checkValid = function() {
document.getElementById('invite_submit').disabled = !validateForm2();
}
if(inputs_invite[1] != null){
    inputs_invite[1].addEventListener('change', checkValid);
    inputs_invite[1].addEventListener('keypress', checkValid);
}

var validateInvite = function validateinvitecontact(){
    console.log("here");
    var cont = form.invitecontact.value;
    var reg = /^[6-9]\d{9}$/;
    if (cont == ""){
        document.getElementById("phnerr").innerHTML = "Please Enter Phone No.";
        document.getElementById("invitecontact").style.border = "1px solid red";
        return false;
    }
     else if (cont.search(reg) == -1) {
    document.getElementById("phnerr").innerHTML = "Enter valid mobile number";
    document.getElementById("invitecontact").style.border = "1px solid red";
    return false;
  }
    else if (cont.length != 10) {
    document.getElementById("phnerr").innerHTML = "Enter 10 digit number only";
    document.getElementById("invitecontact").style.border = "1px solid red";
    return false;
  } else if (cont == "+910000000000") {
    document.getElementById("phnerr").innerHTML = "enter valid no.";
    document.getElementById("invitecontact").style.border = "1px solid red";
    return false;
  } else {
    document.getElementById("phnerr").innerHTML = "";
    document.getElementById("invitecontact").style.border = "1px solid green";
    return true;
  }
}

function checknumber(event) {
  var k = event.keycode || event.which;
  if (k > 47 && k < 58) {
    return true;
  } else {
    return false;
  }
}
function checkcharacter(event) {
  var k = event.keycode || event.which;
  if ((k > 64 && k < 91) || (k > 96 && k < 123)) {
    return true;
  } else {
    return false;
  }
}

//setTimeout(function() {
//  $("#message").fadeOut("slow");
//}, 3000);


var roomName
var friend_username
var last_msg_date = []
function chat_send_receive_socket(room, friend_notify_room, username){
    chatSockets[friend_notify_room] = new WebSocket(
            'wss://' + window.location.host +
            '/ws/chat/' + friend_notify_room + '/');

//    if(last_msg_date[username]==null){
//        alert("null")
//    }
    chatSockets[room].onmessage = function(e) {

        var data = JSON.parse(e.data);
        var message = data['message'];
        msg = message.replace(/(?:\r\n|\r|\n)/g, '<br>');

        var today = new Date();
        hour = today.getHours();
        minute = today.getMinutes();

        if(hour.toString().length == 1 && minute.toString().length == 1){
            var time = "0" + hour + ":0" + minute
        }
        else{

            if(hour.toString().length == 1){
                var time = "0" + hour + ":" + minute
            }
            else if(minute.toString().length == 1){
                var time = hour + ":0" + minute
            }
            else{
                var time = hour + ":" + minute
            }
        }

        if(user==data['username']){
            $('<li class="sent"><p>' + msg + '</p></li><p style="float:right;font-size:11px;padding-right:15px;">'+ time +'</p>').appendTo($('.messages ul'));
            $(".messages").animate({ scrollTop: $(document).height() + 10000}, "fast");

            document.getElementById("pre_"+username).innerHTML = message
              var listItem = document.getElementById("cls_"+username);
              Index =  $( "li" ).index( listItem ) + 1;
              console.log(Index)
              child_click = "#contacts ul li:nth-child("+ Index.toString() +")"

              $("#contacts ul li").on('click', function() {
                  console.log("Clicked")
                  var $myLi = $(this);
                  var listHeight = $("#contacts ul").innerHeight();
                  var elemHeight = $myLi.height();
                  var elemTop = $myLi.position().top;
                  var moveUp = listHeight - (listHeight - elemTop);
                  var moveDown = elemHeight;
                  var liId = $myLi.attr("id");
                  var enough = false;
                  var liHtml = $myLi.outerHTML();

                  $("#contacts ul li").each(function() {
                    if ($(this).attr("id") == liId) {
                        return false;
                    }
                    $(this).animate({"top": '+=' + moveDown}, 300);
                  });

                  $myLi.animate({"top": '-=' + moveUp}, 300, function() {
                    $myLi.remove();
                    var oldHtml = $("#contacts ul").html();
                    $("#contacts ul").html(liHtml + oldHtml);
                    $("#contacts ul li").attr("style", "");
                  });
              });

              (function($) {
                  $.fn.outerHTML = function() {
                    return $(this).clone().wrap('<div></div>').parent().html();
                  }
                })(jQuery);
//                  $(this).parent().prepend(this);
            $(child_click).click();
        }
        else{
            if(roomName==data['room_name']){
                $('<li class="replies"><p>' + message + '</p></li><p style="float:left;font-size:11px;padding-left:22px;">'+ time +'</p>').appendTo($('.messages ul'));
                $(".messages").animate({ scrollTop: $(document).height() + 100000}, "fast");

                $.ajax({
                url: '../chat/seen-message/',
                type: 'POST',
                dataType: 'html',
                data: {message_id: data['msg_id']},
                success: function(json){

                },
                error: function(xhr, errormsg, err){
                alert(xhr);
                }
                });

            }
        }
    };

//    chatSocket.onmessage = function(e) {
//        var data = JSON.parse(e.data);
//        var message = data['message'];
////        if(user==data['username']){
//        alert("Send message");
//        alert("Received message");
//     }
//            $('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));
//            $(".messages").animate({ scrollTop: $(document).height() }, "fast");
//        }
//        else{
//            if(roomName==data['room_name']){
//                $('<li class="replies"><p>' + message + '</p></li>').appendTo($('.messages ul'));
//                $(".messages").animate({ scrollTop: $(document).height() }, "fast");
//            }

    chatSockets[room].onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

//    document.querySelector('#chat-message-input').focus();
//    document.querySelector('#chat-message-input').onkeyup = function(e) {
//        if (e.keyCode === 13) {  // enter, return
//            document.querySelector('#chat-message-submit').click();
//        }
//    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
        var messageInputDom = document.querySelector('#chat-message-input');
        var message = messageInputDom.value;
        chatSockets[room].send(JSON.stringify({
            'message': message,
            'username': user,
            'notification': false,
        }));

        chatSockets[friend_notify_room].send(JSON.stringify({
            'message': message,
            'username': user,
            'notification': "message_notification",
        }));

        messageInputDom.value = '';

    };
}


function loadchat(username){
scroll_count = 1
friend_username = username
//    var friend_info = new Array();
var room = '';
    $.ajax({
         url: '../chat/messages/',
         type: 'POST',
         dataType: 'html',
         data: {username: username},
         success: function(json){
            document.getElementById("message-inputs").style.display = 'block'
            document.getElementById("contact-profile-id").style.display = 'block'

            $.ajax({
                url: '../chat/seen-all-message/',
                type: 'POST',
                dataType: 'html',
                data: {username: username},
                success: function(json){

                },
                error: function(xhr, errormsg, err){
                    alert(xhr);
                }
            })

            data = JSON.parse(json)
            unread_msg_count[data['friend_id']] = 0
            document.getElementById("msg_count_id_"+data['friend_id'].toString()).style.display = 'none';

            document.getElementById("friend-name").innerHTML = data['name']
            document.getElementById("profile-pic").src = data['profile-pic']
            document.getElementById("chat_scrn_full_name").href = "/user_profile/" + username

            chats = data['messages']
            roomName = data['room_name']
            friend_notify_room = data['friend_notify_room']
            chat_send_receive_socket(roomName, friend_notify_room, username);

            $('.messages ul').empty();

            if(!data['same_day']){
                chat_date_reverse_arry = chats[0][1].split(' ')[0].split('-');
                chat_date = chat_date_reverse_arry[2] + '-' + chat_date_reverse_arry[1] + '-' + chat_date_reverse_arry[0]
                $('<li style="text-align:center;"><p><b>'+ chat_date +'<b></p></li>').appendTo($('.messages ul'));
            }

            for(i=0;i<chats.length;i++){
                chats[i][0] = chats[i][0].replace(/(?:\r\n|\r|\n)/g, '<br>');

               var full_time = chats[i][1].split(' ')[1].split('.')[0].split(':')
               if(chats[i][3] == 'same_date'){
                   if(chats[i][2] == 'sent'){
                       $('<li class="sent"><p>' + chats[i][0] + '</p></li><p style="float:right;font-size:11px;padding-right:15px;">'+ full_time[0] +':'+ full_time[1] +'</p>').appendTo($('.messages ul'));
                   }
                   else{
                       $('<li class="replies"><p>' + chats[i][0] + '</p></li><p style="float:left;font-size:11px;padding-left:22px;">'+ full_time[0] +':'+ full_time[1] +'</p>').appendTo($('.messages ul'));
                   }
               }
               else{
                    chat_date_reverse_arry = chats[i][1].split(' ')[0].split('-');
                    chat_date = chat_date_reverse_arry[2] + '-' + chat_date_reverse_arry[1] + '-' + chat_date_reverse_arry[0]

                   if(chats[i][2] == 'sent'){
                       $('<li style="text-align:center;"><p><b>'+ chat_date +'<b></p></li>').appendTo($('.messages ul'));
                       $('<li class="sent"><p>' + chats[i][0] + '</p></li><p style="float:right;font-size:11px;padding-right:15px;">'+ full_time[0] +':'+ full_time[1] +'</p>').appendTo($('.messages ul'));
                   }
                   else{
                       $('<li style="text-align:center;"><p><b>'+ chat_date +'<b></p></li>').appendTo($('.messages ul'));
                       $('<li class="replies"><p>' + chats[i][0] + '</p></li><p style="float:left;font-size:11px;padding-left:22px;">'+ full_time[0] +':'+ full_time[1] +'</p>').appendTo($('.messages ul'));
                   }
               }

            }

            $(".messages").animate({ scrollTop: $(document).height() + 10000}, "fast");
         },
         error: function(xhr, errormsg, err){
            alert(xhr);
         }
    });
    var current = document.getElementsByClassName('active');
    if(current[0] === void(0)){
    console.log(current)

    }
    else{
    console.log(current)

            current[0].className = current[0].className.replace(" active", "");

    }
    document.getElementById("cls_"+username).className += " active";
}


function addfriend(username){

    request_btn_value = document.getElementById("add-friend-"+username).innerHTML
    $.ajax({
         url: '../addfriend/',
         type: 'POST',
         dataType: 'html',
         data: {username: username,request_btn_value: request_btn_value},
         success: function(json){
              data = JSON.parse(json)
              request_btn_value = data['req_btn_title']
              friend_notification_room = data['friend_notification_room']
              document.getElementById("add-friend-"+username).innerHTML = request_btn_value

             // chatSockets[friend_notification_room] = new WebSocket(
              //       'ws://' + window.location.host + '/ws/chat/' + friend_notification_room + '/');
             if(!data['cancel_request']){
                chatSockets[friend_notification_room].send(JSON.stringify({
                    'notification': 'new_request_notification',
                    'message': "lsdjhfjksdz",
                    'username': username,
                }));
             }


         },
         error: function(xhr, errormsg, err){
            alert("Error");
         }
    });

}


function accept_request(username, id){

    $.ajax({
         url: '../accept-request/',
         type: 'POST',
         dataType: 'html',
         data: {username: username},
         success: function(json){
              data = JSON.parse(json);
              $('#tr-'+id).remove();

              logged_in_users_username = data['logged_in_users_username'];
              friend_notification_room = data['friend_notification_room'];
              chatSockets[friend_notification_room].send(JSON.stringify({
                    'notification': 'accept_request_notification',
                    'message': "lsdjhfjksdz",
                    'username': logged_in_users_username,
                }));
         },
         error: function(xhr, errormsg, err){
            alert("Error");
         }
    });
}


function decline_request(username, id){
    $.ajax({
         url: '../decline-request/',
         type: 'POST',
         dataType: 'html',
         data: {username: username},
         success: function(json){
              data = JSON.parse(json);
              $('#tr-'+id).remove();
         },
         error: function(xhr, errormsg, err){
            alert("Error");
         }
    });
}


var scroll_count = 1
$('.messages').scroll(function(){
    if($('.messages').scrollTop() == 0){
        $.ajax({
         url: '../chat/load-more-chat/',
         type: 'POST',
         dataType: 'html',
         data: {scroll_count: scroll_count,username: friend_username},
         success: function(json){
              data = JSON.parse(json)
              scroll_count = data['scroll_count']
              load_messages = data['load_messages']
              next_message = data['next_message']
              var msg_load = document.getElementById("msg_loader");
              if(next_message=='True'){

                  for(var i=0;i<load_messages.length;i++){

                      var full_time = load_messages[i][1].split(' ')[1].split('.')[0].split(':')
                      msg_load.style.display = 'block'

                      if(load_messages[i][3] == 'same_date'){
                           if(load_messages[i][2] == 'sent'){
                                $('.messages ul').prepend('<li class="sent"><p>' + load_messages[i][0] + '</p></li><p style="float:right;font-size:11px;padding-right:15px;">'+ full_time[0] +':'+ full_time[1] +'</p>');
                           }
                           else{
                                $('.messages ul').prepend('<li class="replies"><p>' + load_messages[i][0] + '</p></li><p style="float:left;font-size:11px;padding-left:22px;">'+ full_time[0] +':'+ full_time[1] +'</p>');
                           }
                      }
                      else{
                           chat_date_reverse_arry = load_messages[i][1].split(' ')[0].split('-');
                           chat_date = chat_date_reverse_arry[2] + '-' + chat_date_reverse_arry[1] + '-' + chat_date_reverse_arry[0]

                           if(load_messages[i][2] == 'sent'){
                               $('.messages ul').prepend('<li class="sent"><p>' + load_messages[i][0] + '</p></li><p style="float:right;font-size:11px;padding-right:15px;">'+ full_time[0] +':'+ full_time[1] +'</p>');
                               $('.messages ul').prepend('<li style="text-align:center;"><p><b>'+ chat_date +'<b></p></li>');
                           }
                           else{
                               $('.messages ul').prepend('<li class="replies"><p>' + load_messages[i][0] + '</p></li><p style="float:left;font-size:11px;padding-left:22px;">'+ full_time[0] +':'+ full_time[1] +'</p>');
                               $('.messages ul').prepend('<li style="text-align:center;"><p><b>'+ chat_date +'<b></p></li>');
                           }
                      }




//                      if(load_messages[i][2] == 'sent'){
//                          $('.messages ul').prepend('<li class="sent"><p>' + load_messages[i][0] + '</p></li><p style="float:right;font-size:11px;padding-right:15px;">'+ full_time[0] +':'+ full_time[1] +'</p>');
//                      }
//                      else{
//                          $('.messages ul').prepend('<li class="replies"><p>' + load_messages[i][0] + '</p></li><p style="float:left;font-size:11px;padding-left:22px;">'+ full_time[0] +':'+ full_time[1] +'</p>');
//                      }

                  }
                  setTimeout(function(){
                    // Simulate retrieving 4 messages
                    $('.messages').scrollTop(100);
                  },1000);
//                  msg_load.setAttribute('style', 'display:none !important');
//                  document.getElementById("msg_loader").style.display = 'none !important'

              }
              else{
                  msg_load.setAttribute('style', 'display:none !important');
              }




//              $('.messages').scrollTop(30);
         },
         error: function(xhr, errormsg, err){
            alert("Error");
         }
    });

//        setTimeout(function(){
//        // Simulate retrieving 4 messages
//            for(var i=0;i<2;i++){
//                $('.messages ul').prepend('<li class="sent"><p>XYZ</p></li>');
//            }
//            $('.messages').scrollTop(30);
//        },1000);
    }
})


$('#notification').click(function(){
    document.getElementById('new_notifications_count').innerText = "";
});
$('#settings').click(function(){
    alert("This feature will coming soon.")
});

$('#chatBox').scroll(function(){
    if ($('#chatBox').scrollTop() == 0){
        // Display AJAX loader animation
//         $('#loader').show();

      // Youd do Something like this here
      // Query the server and paginate results
      // Then prepend
      /*  $.ajax({
            url:'getmessages.php',
            dataType:'html',
            success:function(data){
                $('.inner').prepend(data);
            };
        });*/
        //BUT FOR EXAMPLE PURPOSES......
        // We'll just simulate generation on server


        //Simulate server delay;
        setTimeout(function(){
        // Simulate retrieving 4 messages
        for(var i=0;i<4;i++){
        $('.inner').prepend('<div class="messages">Newly Loaded messages<br/><span class="date">'+Date()+'</span> </div>');
            }
            // Hide loader on success
            $('#loader').hide();
            // Reset scroll
            $('#chatBox').scrollTop(30);
        },2000);
    }
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            }
        }
    });
});


$(document).ready(function () {
  $('#dtBasicExample').DataTable({  "language": {
  "searchPlaceholder": "Search by Name & No.",
   "search": "Search:",
    "paginate": {
      "previous": "<<",
      "next": ">>",
    },
    "sEmptyTable": "No more contact to add as friend",
  }});
  $('.dataTables_length').addClass('bs-select');
});


$(document).ready(function () {
  $('#data').DataTable({  "language": {
    "searchPlaceholder": "Name",
   "search": "Search:",
    "paginate": {
      "previous": "<<",
      "next": ">>"
    }
  }});
  $('.dataTables_length').addClass('bs-select');
});


var perfEntries = performance.getEntriesByType("navigation");

if (perfEntries[0].type === "back_forward") {
    location.reload(true);
}


//jQuery( document ).ready(function( $ ) {
//
//   //Use this inside your document ready jQuery
//   $(window).on('popstate', function() {
//      location.reload(true);
//   });
//
//});


$('textarea#chat-message-input').keydown(function (e) {
    if (e.keyCode === 13 && e.ctrlKey) {
        //console.log("enterKeyDown+ctrl");
        $(this).val(function(i,val){
            return val + "\n";
        });
    }
}).keypress(function(e){
    //mehaahah
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
        if(e.preventDefault) e.preventDefault();
    }
});










