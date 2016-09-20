
host='http://localhost:8001/records/'

    //文档就绪函数
$(document).ready(function(){

      get_records_content();
});


function get_records_content(){
	$.ajax({
		url:host,
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
					create_type_program_html(object)
				}else if (object.record_type == "type_travel") {
					create_type_travel_html(object)
				}
			}
		},
		error:function (error){
			console.log(error)
		}
	})

}



function create_type_video_html(object){
	
	
}

function create_type_phtoto_html(object){
	console.log(object)
	
}

function create_type_travel_html(object){
	console.log(object)
}

function create_type_program_html(object){
	console.log(object)
}