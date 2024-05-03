d3.selection.prototype.moveToFront = function() {
  return this.each(function(){
  this.parentNode.appendChild(this);
  });
};

const container = d3.select('svg')
	.attr("viewBox", "0 0 1000 589"); 

function makeURL(data) {
	return "/" + data; 
}

d3.csv("../static/statepath.csv", function(data){
	container.selectAll('path') 
		.data(data)
		.enter()
		.append('a')
		.attr('href', data => makeURL(data.state))
		.on("mouseover",function(){
		var sel = d3.select(this);
		sel.moveToFront();
		})
		.append('path')	
		.attr({
		id: data => data.state,
		d: data => data.d
		});
});


 
