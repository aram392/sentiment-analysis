
// $(document).ready(function(){
//     //connect to the socket server.
//     var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
//     var comments = [];

//     //receive details from server
//     socket.on('newcomment', function(msg) {
//         console.log("Received comment" + msg.comment);
//         if (comments.length >= 10){
//             comments.shift()
//         }            
//         comments.push(msg.comment);
//         commentString = '';
//         for (var i = 0; i < comments.length; i++){
//             commentString = commentString + '<p>' + comments[i].toString() + '</p>';
//         }
//         $('#log').html(commentString);
//     });

// });

// $(document).ready(function(){
//     //connect to the socket server.
//     var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
//     var numbers_received = [];

//     //receive details from server
//     socket.on('newnumber', function(msg) {
//         console.log("Received number" + msg.number2);
      
//         var h2=msg.number2
//         //maintain a list of ten numbers
//         if (numbers_received.length >= 10){
//             numbers_received.shift()
//         }            
//         numbers_received.push(h2);
//         numbers_string = '';
//         for (var i = 0; i < numbers_received.length; i++){
//             numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
//         }
//         $('#log').html(numbers_string);
//     });

// });