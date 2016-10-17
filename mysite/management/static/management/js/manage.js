
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
				//移除之前内容
				remove_tableview_content()
				//添加内容
				for (var i = 0; i < content.list.length; i++) {
					create_list_view(content.list[i])
				}
			},
			error:function(error){
				console.log(error)
		}
	})
}

//创建cell
function create_list_view(object){
	var $container=$(".table_view") //获取容器
	var $template=$("script#list_template") //cell模板

	var $elem=$($template.html())
	$elem.find(".title").text(object.title)

	$container.append($elem)
}

//移除
function remove_tableview_content(){
	var $container=$(".table_view") //获取容器
	var $template=$("script#list_template") //cell模板

	$container.empty()
	
}	








