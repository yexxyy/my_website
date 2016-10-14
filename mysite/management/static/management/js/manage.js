
host='http://'+window.location.host


$(document).ready(function(){
	
	get_list("")
	navbar_click()
})

//导航栏点击事件
function navbar_click(){

	$("#demo-navbar .container  a").click(function(){
		//让展开视图缩回
		var expanded_change=$("#bs-example-navbar-collapse-1")
		expanded_change.removeClass('in').attr({'aria-expanded':'false'})

		//获取对应列表数据
		var type_str=$(this).attr("href").slice(1)
		get_list(type_str)
	})
}

//根据类型获取对应列表
function get_list(type_str){
	temp_url=host+'/management'+'/record/'+type_str,
		$.ajax({
			url:temp_url,
			type:'get',
			success:function(content){
				console.log(content)
			},
			error:function(error){
				console.log(error)
		}
	})
}