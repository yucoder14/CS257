function statePopulation(city,population) {
	return city + ", {{state}} has population of " + population; 
}

const parsed = d3.csv.parse("{{cities}}");
console.log(parsed);
d3.select('ol').selectAll('li')
	.data(parsed)
	.enter()
	.append('li')
	.text(data => statePopulation(data.city,data.population));
