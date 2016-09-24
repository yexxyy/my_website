
host='http://localhost:8001'

//全局变量,用于保存发布时间
var temp_publish_date
var current_date
var yestoday_date 
    //文档就绪函数
$(document).ready(function(){

      get_records_content()
      get_current_date()

})

function get_current_date(){
	current_date=get_date_string(0)
	yestoday_date=get_date_string(-1)
}

function get_date_string(count){ 
	var dd = new Date()
	dd.setDate(dd.getDate()+count)//获取AddDayCount天后的日期 
	var year = dd.getFullYear()
	var month = dd.getMonth()+1;//获取当前月份的日期 
	var day = dd.getDate()
	result_date=year+'-'+(month<10?'0'+month:month)+'-'+(day<10?'0'+day:day)
	console.log('获取的日期：'+result_date)
	return result_date
} 

function get_records_content(){
	$.ajax({
		url:host+'/record/',
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

	var temp_Publish_label=$elem.find('.publish_time')
	
	if (temp_publish_date!=object.publish_date) {

		switch (object.publish_date){
			case current_date:{
				temp_Publish_label.text('今天')
				break
			}
			case yestoday_date:{
				temp_Publish_label.text('昨天')
				break
			}
			default :{
				temp_Publish_label.text(object.publish_date)
				break
			}
		}
		temp_publish_date=object.publish_date
		$elem.find('.devider').attr('width',0)
	}

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

	var temp_Publish_label=$elem.find('.publish_time')

	if (temp_publish_date!=object.publish_date) {

		switch (object.publish_date){
			case current_date:{
				temp_Publish_label.text('今天')
				break
			}
			case yestoday_date:{
				temp_Publish_label.text('昨天')
				break
			}
			default :{
				temp_Publish_label.text(object.publish_date)
				break
			}
		}
		temp_publish_date=object.publish_date
		$elem.find('.devider').attr('width',0)
		$elem.find('publish_time').attr('height',80)
	}
	
	$elem.find('.title').text(object.title)
	$elem.find('.description').text(object.article_description)

	$container.append($elem) //在容器结尾放入元素

}

