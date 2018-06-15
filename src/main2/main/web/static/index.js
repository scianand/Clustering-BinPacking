const postData = (url, data) => {
	return fetch(url, {
		body: JSON.stringify(data),
		headers: { 'content-type': 'application/json' },
		method: 'POST',
		cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		redirect: 'follow', // manual, *follow, error
		referrer: 'no-referrer', // *client, no-referrer
		mode: 'cors'
	}).catch((error) => console.log(error)).then((response) => response.json())
}

const readFile = async (file) => {
	var reader = new FileReader();
	return new Promise((resolve, reject) => {
		reader.onload = function (e) {
			resolve(reader.result);
		}
		reader.readAsText(file);
	});
}

window.onload = async () => {
	var fileInput = document.getElementById('fileInput');
	var fileDisplayArea = document.getElementById('fileDisplayArea');
	var button1 = document.getElementById('button1');
	var choosealgo = document.getElementById('select1');

	fileInput.addEventListener('change', async () => {

	});

	button1.addEventListener('click', async () => {

		if (choosealgo.selectedIndex == 0) {
			let csvString = await readFile(fileInput.files[0]);
			let config = {
				header: true,
				skipEmptyLines: true,
				dynamicTyping: true
			};
			let json = Papa.parse(csvString, config).data;
			console.log("CSV -> JSON: done");
			// "http://" + location.hostname + ":5000/api/test"
			let apiResult = await postData(`http://${location.hostname}:5000/api/test`, json);
			for (let i = 0; i < apiResult.hello.length; i++) {
				console.log(apiResult.hello[i]);
				fileDisplayArea.innerHTML += apiResult.hello[i].collection_date;
				fileDisplayArea.innerHTML += "\n";
			}
		}
	});
}
