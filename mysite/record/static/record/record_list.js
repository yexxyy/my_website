
host='http://localhost:8001'


    //文档就绪函数
$(document).ready(function(){

      get_records_content();
});


function get_records_content(){
	$.ajax({
		url:host+'/records/',
		type:'get',
		success:function (content){
			console.log(content.list)
			list=content.list
			for (var i = 0; i < list.length; i++) {
				object=list[i]
				if (object.record_type == "type_video") {
					create_type_video_html(object)
				}else if (object.record_type == "type_phtoto") {
					create_type_phtoto_html(object)
				}else if (object.record_type == "type_program") {
					create_type_travel_program_html(object)
				}else if (object.record_type == "type_travel") {
					create_type_travel_program_html(object)
				}
			}
		},
		error:function (error){
			console.log(error)
		}
	})

}



function create_type_video_html(object){
	var $container = $('.table_view')//容器
	var $template = $('script#video_template')//模版

    var cover_url = host+object.banner;
	var $elem = $($template.html())
	$elem.find('.description').text(object.article_description)
    $elem.find('.banner').attr('src', cover_url)
    $elem.find('.video').text(object.video)


	$container.append($elem) //在容器结尾放入元素
}

function create_type_phtoto_html(object){
	console.log(object)
	
}

function create_type_travel_program_html(object){
	var $container=$('.table_view')
	var $template=$('script#text_template')

	var $elem=$($template.html())
	$elem.find('.title').text(object.title)
	$elem.find('.description').text(object.article_description)

	$container.append($elem) //在容器结尾放入元素

}

