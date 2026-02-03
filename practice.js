// let abcd=document.querySelector("#abcd");
// // abcd.addEventListener("mouseover",function(){
// //     abcd.style.backgroundColor="red" ;
// // });
// // abcd.addEventListener("mouseout",function(){
// //     abcd.style.backgroundColor="green" ;
// // });


// // window.addEventListener("mousemove",function(dets){
// //    abcd.style.top=dets.clientY+"px";
// //    abcd.style.left=dets.clientX+"px";
// // });

// // let ul=document.querySelector("ul");
// // ul.addEventListener("click",function(dets){
// // dets.target.classList.toggle("li");
// // });

// // let inp=document.querySelector("input");
// // let span=document.querySelector("span");
// // inp.addEventListener("input",function(dets){
// // // span.textContent=inp.value.length;
// // let left=20-inp.value.length;
// // span.textContent=left;
// // if(left<0){
// //    span.style.color="red";
// // }
// // else{
// //    span.style.color="black";
// // }

// // })

// let container = document.querySelector(".download-container")
// let progress=document.querySelector(".progress-bar");

// container.addEventListener("click",function(){
//    let count=0;
//    let int=setInterval(function(){
//       if(count<=99){
//          count++;
//          progress.style.width=`${count}%`;
//          document.querySelector("#percent").textContent=`${count}%`;
//       }
//       else{
//          document.querySelector("h2").textContent="File downloaded";
//          document.querySelector("#percent").textContent="Download finished wow 🎉";      }
//    },50)
// });


// if(localStorage.getItem("theme")){
//    document.body.classList.add(localStorage.getItem("theme"))
// }

// let btn=document.querySelector("button");

// btn.addEventListener("click" , function(){
// if(document.body.classList.contains("dark")){
// document.body.classList.remove("dark");
// document.body.classList.add("light");
// localStorage.setItem("theme",light);
// }
// else{
//    document.body.classList.remove("light");
// document.body.classList.add("dark");
// localStorage.setItem("theme",dark);

// }
// })




