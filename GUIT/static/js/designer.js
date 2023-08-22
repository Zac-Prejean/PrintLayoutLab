

  
document.querySelector("form").addEventListener("submit", async (e) => {  
e.preventDefault();  
const formData = new FormData(e.target);  
const response = await fetch("/run-script", {  
method: "POST",  
body: formData,  
});  
const result = await response.json();  
document.getElementById("result").textContent = result.message || result.error;  
});  
