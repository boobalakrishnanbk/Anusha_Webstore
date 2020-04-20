function activechanger(){
  active = document.getElementById('active').value;
  loop = document.getElementsByName(active);
  for (var i=0; i<loop.length; i++){
    loop[i].className += ' active';
  }
}

function searchEmployee() {
    var input = document.getElementById('search');
    var table = document.getElementById('employee_details');
    var table_row = document.getElementsByTagName('tr');
    var filter = input.value.toUpperCase();
    for (var i = 0; i < table_row.length; i++) {
      var td = table_row[i].getElementsByTagName('td')[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          table_row[i].style.display = "";
        } else {
          table_row[i].style.display = "none";
        }
      }
    }
}



function searchEmployee_attendance() {
    var input = document.getElementById('search');
    console.log('hi');
    var table = document.getElementById('employee_details');
    var table_row = document.getElementsByTagName('tr');
    var filter = input.value.toUpperCase();
    for (var i = 0; i < table_row.length; i++) {
      var td = table_row[i].getElementsByTagName('td')[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          table_row[i].style.display = "";
        } else {
          table_row[i].style.display = "none";
        }
      }
    }
}
//
// // function filtername() {
// //   var input, filter, table, tr, td, i, txtValue;
// //   input = document.getElementById("name");
// //   filter = input.value.toUpperCase();
// //   table = document.getElementById("myTable");
// //
// //   tr = table.getElementsByTagName("tr");
// //   for (i = 0; i < tr.length; i++) {
// //     td = tr[i].getElementsByTagName("td")[0];
// //     if (td) {
// //       txtValue = td.textContent || td.innerText;
// //       if (txtValue.toUpperCase().indexOf(filter) > -1) {
// //         tr[i].style.display = "";
// //       } else {
// //         tr[i].style.display = "none";
// //       }
// //     }
// //   }
// //   if (tr.length >0){
// //     tb = table.getElementsByTagName('table');
// //     for (var i = 0; i < tb.length; i++) {
// //       tb[i] = .style.display = "none";
// //     }
// //   }
// //
// // }
//
//
// function checkall1(){
//   console.log(this.value);
//
//
//   // console.log(document.getElementById('shift1').checked);
// }
//   if (document.getElementById('shift1').checked == true)
//   {
//     check = document.getElementsByClassName('shift1');
//     for (var i = 0; i < check.length; i++)
//     {
//       check[i].checked = true;
//     }
//   }
//   else if (document.getElementById('shift2').checked == true)
//   {
//     check = document.getElementsByClassName('shift2');
//     for (var i = 0; i < check.length; i++)
//     {
//       check[i].checked = true;
//     }
//   }
//   else
//   {
//     check = document.getElementsByClassName('shift3');
//     for (var i = 0; i < check.length; i++)
//     {
//       check[i].checked = true;
//     }
//   }
// }
// $(document).ready(()=> {
//   // filtername = $('input#filtername').val();
//   filterlocation = $('input#filterlocation').val();
//   filterdesignation = $('input#filterdesignation').val();
//   filterworkingstate = $('input#filterworkingstate').val();
//   filterlocality = $('input#filterlocality').val();
//
//
//   setttings_active = $('input#setttings_active').val();
//
//   // console.log(filterworkingstate);setttings_active
//   // $('#name').val(filtername)
//
//   $('#farmlocation').val(filterlocation)
//   $('#designation').val(filterdesignation)
//   $('#state').val(filterworkingstate)
//   $('#locality').val(filterlocality)
//
//   if (setttings_active == 'options') {
//     $('#options').addClass(" show")
//   }
//   else if (setttings_active == 'salary') {
//     $('#salary').addClass(" show")
//   }
//   else {
//     $('#manager').addClass(" show")
//   }
//   console.log(setttings_active);
//   console.log(  $('#options').attr('class'));
//   console.log(  $('#salary').attr('class'));
//   console.log(  $('#manager').attr('class'));
//
// })
// $(document).ready(function(){
//   $("button").click(function(){
//     $("h1, h2, p").addClass("blue");
//     $("div").addClass("important");
//   });
// });
