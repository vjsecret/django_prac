// JavaScript Document
(function(){ //立即匿名
      // Initialize Firebase
        var config = {
                apiKey: "AIzaSyBBpKMDQk2He3D3uPVrypr0namRTJes2pk",
                authDomain: "first20190109.firebaseapp.com",
                databaseURL: "https://first20190109.firebaseio.com",
                projectId: "first20190109",
                storageBucket: "first20190109.appspot.com",
                messagingSenderId: "1026634990833"
              };
              firebase.initializeApp(config);
		const txtEmail=document.getElementById('txtEmail');
		const txtPwd=document.getElementById('txtPwd');
		const btnLogin=document.getElementById('btnLogin');
        const liMana=document.getElementById('mana');
		const liSignUp=document.getElementById('liSignUp');
        const auth=firebase.auth();

		btnLogin.addEventListener('click',e=>{
								var email=txtEmail.value;
								var pwd=txtPwd.value;							
								var promise=auth.signInWithEmailAndPassword(email, pwd);
		
								promise.then(function(){
										alert("歡迎光臨!!");
										//authDemo.innerHTML="電子郵件:"+email+"<br>";
									});
								promise.catch(error=>{
											  if (error.code==="auth/invalid-email")
												alert("電子郵件格式不正確!!");
											else if (error.code==="auth/user-not-found")
												alert("無此使用者!!");
											else if (error.code==="auth/wrong-password")
												alert("密碼錯誤!!");
											else
												alert("登入失敗，可能被停權了，請主動與MIS人員聯絡!!");
												//authDemo.innerHTML="登入失敗訊息:"+error.message+"<br>";
									});
		
		});
		

        btnLogout.addEventListener('click',e=>{							
                auth.signOut();
                alert("881~~");
				txtEmail.value='';
				txtPwd.value='';
				//javascript:location.href='login2';
            });
        
        auth.onAuthStateChanged(firebaseUser=>{
                                  if(firebaseUser){
                    console.log(firebaseUser);
                    btnLogout.style.display="inline-block";
                    liMana.style.display="inline-block";
					txtEmail.style.display="none";
					txtPwd.style.display="none";
					btnLogin.style.display="none";
                    liSignUp.style.display="none";                    
                    }else{
                    btnLogout.style.display="none";
                    liMana.style.display="none";
					txtEmail.style.display="inline-block";
					txtPwd.style.display="inline-block";
					btnLogin.style.display="inline-block";
                    liSignUp.style.display="inline-block";
                }
        });


}());