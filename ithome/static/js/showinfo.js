// JavaScript Document
(function(){ //立即匿名
//function addItem(){
const addCar=document.getElementById('addCar');
//addCar.bind("click",function(){
addCar.addEventListener('click',function(){
									console.log(this.name);
									const it=this.name;
									const t1 = document.getElementsByClassName("card-title")[it].innerHTML;
									console.log(t1)
									//var b = document.getElementById("content").getElementsByClassName("price")[it].value;
									var b = document.getElementsByClassName("price")[it].innerHTML;
									console.log(b);
									console.log(b.value);
									const a="price";	
									items = {};
									items["title"]=t1;
									items[a]=b;
									//items["price"]="180";
									console.log(items);
									
									//const title=document.getElementById('title');
									//const price=document.getElementById('price');
									//console.log(title.innerHTML);
									//console.log(price.innerHTML);
									////title.val()=title.innerHTML;
									////price.val()=price.innerHTML;									
									//console.log(title.value);
									//console.log(price.value);
									////$.ajax({method:"POST",data:{title: title.innerHTML,price: price.innerHTML}}).done(function(msg)){alert("Data save"+ msg);};
									//$("#addCar").submit();
									//alert("Handler for .submit() called.");
									////$( "#addCar" ).submit(function( event ) {  alert( "Handler for .submit() called." );
									////event.preventDefault();});

									$.ajax({
									url: '/addCar',
									type: 'POST',
									data: items,
									dataType: 'json',
									timeout: 100,									
									success: function(result) {
									//console.log(result.result);
									if ( result.result == "post_success" ) {
										//$("#ntfText").html("發起成功");
										$("#ntfText").html(result.result);
										}else {
										$("#ntfText").html("重複發起了");
											}
										}
									});
								
							});//end of addCar.addEventListener

const content=document.getElementById('content');
/*
									  var childKey=childsnap.key;		 //記錄子項key;
									  var childVal=childsnap.val();         //記錄子項的值(物件)
									  var r= tblProduct.insertRow(rIndex); //插入列
									  var celSrc=r.insertCell(0); //列裡插入第1格								
									  var celName=r.insertCell(1); //列裡插入第2格
									  var celprice=r.insertCell(2); //列裡插入第3格
									  var celTQuant=r.insertCell(3); //列裡插入第4格
									  var celTprice=r.insertCell(4); //列裡插入第5格
									  var box=r.insertCell(5); //列裡插入第0格
									  childVal.name=childVal.name.replace(/'/g,''); //消除從FIRBASE在入時的'
									  		
										.appendChild(document.createElement('div'));											
									  img1=celSrc.appendChild(document.createElement('img'));
									  .appendChild(document.createElement('div'));
									  .appendChild(document.createElement('a'));
									  .appendChild(document.createElement('h5'));
									  {% if infolist.content %}
									  .appendChild(document.createElement('p'));
									  {% endif %}
									  {% if infolist.price %}
									  .appendChild(document.createElement('p'));									  
									  .appendChild(document.createElement('form'));
									  .appendChild(document.createElement('input'));
									  .appendChild(document.createElement('input'));
									  .appendChild(document.createElement('button'));
									  {% endif %}
									  
									  celName.appendChild(document.createTextNode(childVal.name));
									  celprice.appendChild(document.createTextNode(childVal.price));
									  celTQuant.appendChild(document.createTextNode(childVal.TQuant));
									  celTprice.appendChild(document.createTextNode(childVal.Tprice));
									  btn1=box.appendChild(document.createElement('button'));
									  rIndex=rIndex+1;
									  total=total+childVal.Tprice;							  
									  img1.src=childVal.src;
									  img1.width=70
									  img1.hight=70	
									  btn1.id=childKey;
									  //btn1.setAttribute("onclick", "deleteFun()")
									  //btn1.onclick =deleteFun();
									  btn1.innerHTML="刪除訂單"; 
									  console.log(childKey); 
									  
/*									  var btn1=document.getElementById(childKey);
									  console.log(btn1)
									  btn1.addEventListener('click', function(){
									  dbRefProduct.remove()
										  .then(function() {
											console.log("Remove succeeded.")
											alert("訂單移除成功")
											}).catch(function(error) {
											console.log("Remove failed: " + error.message)
											alert("訂單移失敗"+error.message)})
												  });/
												  
												})//子項 
									  $("p").append("本次購物總金額:"+total);
									  console.log(total);*/
//}// end of addItem();

}());