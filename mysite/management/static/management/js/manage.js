
host='https://'+window.location.host


$(document).ready(function(){
	navbar_click()
	

})

//导航栏点击事件
function navbar_click(){

	$("#demo-navbar .container  a").click(function(){
		//模拟点击事件,让展开视图缩回
		var expanded_change_btn=$("#bs-example-navbar-collapse-1")
		expanded_change_btn.removeClass('in').attr({'aria-expanded':'false'})

		var type_str=$(this).attr("href").slice(1)
		console.log(type_str)

	})


}