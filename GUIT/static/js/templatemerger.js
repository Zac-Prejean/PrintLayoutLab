
// Array to store the loaded PNGs
const loadedPNGs = [];

const fileInput = document.getElementById('file-input');
  const previewArea = document.getElementById('preview-area');
  const exportButton = document.getElementById('export-button');

  // Add event listeners to the file input and export button
  fileInput.addEventListener('change', handleFileInputChange);
  exportButton.addEventListener('click', handleExportButtonClick);



// Function to change through formats
document.querySelector("#desk-plates").addEventListener("click", function () {
  const dropdown = document.querySelector("#format-btn");
  dropdown.innerText = "Desk Plates";
});

document.querySelector("#flutes").addEventListener("click", function () {
  const dropdown = document.querySelector("#format-btn");
  dropdown.innerText = "Flutes";
});

document.querySelector("#rings").addEventListener("click", function () {  
  const dropdown = document.querySelector("#format-btn");  
  dropdown.innerText = "Rings";  
});

document.querySelector("#one-name-neckless").addEventListener("click", function () {  
  const dropdown = document.querySelector("#format-btn");  
  dropdown.innerText = "One Name Neckless";  
});

document.querySelector("#two-name-neckless").addEventListener("click", function () {  
  const dropdown = document.querySelector("#format-btn");  
  dropdown.innerText = "Two Name Neckless";  
});

document.querySelector("#three-name-neckless").addEventListener("click", function () {  
  const dropdown = document.querySelector("#format-btn");  
  dropdown.innerText = "Three Name Neckless";  
});

document.querySelector("#four-name-neckless").addEventListener("click", function () {  
  const dropdown = document.querySelector("#format-btn");  
  dropdown.innerText = "Four Name Neckless";  
});


// Handle file input change event
function handleFileInputChange(event) {
  previewArea.innerHTML = '';
  loadedPNGs.length = 0;
  const files = event.target.files;
  let counter = 0;

  for (let i = 0; i < files.length; i++) {
    const file = files[i];

    const reader = new FileReader();

    reader.onload = function (e) {
      const img = new Image();

      img.onload = function () {
        loadedPNGs.push(img);
        counter++;
        if (counter === files.length) {
          generatePreview();
        }
      };

      img.src = e.target.result;
      previewArea.appendChild(img);
    };
    reader.readAsDataURL(file);
  }
}

function handleExportButtonClick() {
  
// DESK PLATES

  if (document.querySelector("#format-btn").innerText === "Desk Plates") {

  const files = document.getElementById('file-input').files;
  if (files.length > 28) {
    alert('Error: You can only select up to 28 images.');
    return;
  }
  generatePreview();
  setTimeout(() => {

    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const canvasWidthInches = 24;
    const canvasHeightinches = 36;
    const dpi72 = 72.01558002 * 5;
    const canvasWidth = canvasWidthInches * dpi72;
    const canvasHeight = canvasHeightinches * dpi72;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    for (let i = 0; i < loadedPNGs.length; i++) {
      const loadedPNG = loadedPNGs[i];

      const positions = [  
        [1.03, 0.93],  
        [15.38, 0.93],  
        [1.03, 3.446],  
        [15.38, 3.446],  
        [1.03, 5.962],  
        [15.38, 5.962],  
        [1.03, 8.478],  
        [15.38, 8.478],  
        [1.03, 10.994],  
        [15.38, 10.994],  
        [1.03, 13.51],  
        [15.38, 13.51],  
        [1.03, 16.026],  
        [15.38, 16.026],  
        [1.03, 18.542],  
        [15.38, 18.542],  
        [1.03, 21.058],  
        [15.38, 21.058],  
        [1.03, 23.574],  
        [15.38, 23.574],  
        [1.03, 26.09],  
        [15.38, 26.09],  
        [1.03, 28.606],  
        [15.38, 28.606],  
        [1.03, 31.122],  
        [15.38, 31.122],  
        [1.03, 33.638],  
        [15.38, 33.638],  
        [1.03, 36.154],  
        [15.38, 36.154],  
      ];  
        
      let x, y, width, height;  
      if (i < positions.length) {  
        x = positions[i][0] * dpi72;  
        y = positions[i][1] * dpi72;  
        width = 8.08 * dpi72;  
        height = 2 * dpi72;  
      } else {  
        x = i % 2 === 0 ? canvasWidth - (8 * dpi72) : canvasWidth / 24;  
        y = Math.floor((i - 1) / 2) * (2 * dpi72) + canvasHeight / 36;  
        width = 8.08 * dpi72;  
        height = 2 * dpi72;  
      }  
      

    if (i < 28) {
      ctx.save();
      ctx.translate(x + width / 2, y + height / 2);
      ctx.rotate(Math.PI);
      ctx.scale(-1, 1);
      ctx.drawImage(loadedPNG, -width / 2, -height / 2, width, height);
      ctx.restore();
    } else {
      ctx.drawImage(loadedPNG, x, y, width, height);
    }
  }
    const dataURL = canvas.toDataURL('image/png', 1);
    const blob = dataURLToBlob(dataURL);
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'desk_plates.png';
    link.click();
  }, 100);
} 

  
// FLUTES

else if (document.querySelector("#format-btn").innerText === "Flutes") {

  const files = document.getElementById('file-input').files;
  if (files.length > 10) {
    alert('Error: You can only select up to 10 images.');
    return;
  }
    generatePreview();
    setTimeout(() => {

      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');

      const canvasWidthInches = 18.504;
      const canvasHeightinches = 18.504;
      const dpi72 = 70.05406617 * 10;
      const canvasWidth = canvasWidthInches * dpi72;
      const canvasHeight = canvasHeightinches * dpi72;
      canvas.width = canvasWidth;
      canvas.height = canvasHeight;

      for (let i = 0; i < loadedPNGs.length; i++) {
        const loadedPNG = loadedPNGs[i];

         const positions = [  
          [2.25, 0.95],  
          [11.35, 0.95],  
          [2.25, 4.75],  
          [11.35, 4.75],  
          [2.25, 8.55],  
          [11.35, 8.55],  
          [2.25, 12.35],  
          [11.35, 12.35],  
          [2.25, 16.15],  
          [11.35, 16.15],  
        ];  
          
        let x, y, width, height;  
        if (i < positions.length) {  
          x = positions[i][0] * dpi72;  
          y = positions[i][1] * dpi72;  
          width = 4.5 * dpi72;  
          height = 1.5 * dpi72;  
        } else {  
          x = i % 2 === 0 ? canvasWidth - (8 * dpi72) : canvasWidth / 18.504;  
          y = Math.floor((i - 1) / 2) * (2 * dpi72) + canvasHeight / 18.504;  
          width = 4.5 * dpi72;  
          height = 1.5 * dpi72;  
        }  
  
      if (i < 10) {
        ctx.save();
        ctx.translate(x + width / 2, y + height / 2);
        ctx.rotate(Math.PI);
        ctx.drawImage(loadedPNG, -width / 2, -height / 2, width, height);
        ctx.restore();
      } else {
        ctx.drawImage(loadedPNG, x, y, width, height);
      }
    }
  
      const dataURL = canvas.toDataURL('image/png', 1);
      const blob = dataURLToBlob(dataURL);
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'flutes.png';
      link.click();
    }, 100);
  }

  
// JEWELRY
function generateJewelryCanvas(numFilesLimit, fileName) {  
  const files = document.getElementById('file-input').files;  
  if (files.length > numFilesLimit) {  
    alert(`Error: You can only select up to ${numFilesLimit} images.`);  
    return;  
  }  
  generatePreview();  
  setTimeout(() => {  
    const canvas = document.createElement('canvas');  
    const ctx = canvas.getContext('2d');  
  
    const canvasWidthInches = 24;  
    const dpi72 = 72.01558002 * 5;  
    const canvasWidth = canvasWidthInches * dpi72;  
  
    const numRows = Math.ceil(loadedPNGs.length / 2);  
  
    const paddingY = 100;  
    const canvasHeight = numRows * (loadedPNGs[0].height + paddingY) + paddingY;  
    canvas.width = canvasWidth;  
    canvas.height = canvasHeight;  
  
    for (let i = 0; i < loadedPNGs.length; i++) {  
      const loadedPNG = loadedPNGs[i];  
      const col = i % 2;  
      const row = Math.floor(i / 2);  
      const x = col * (canvasWidth / 2);  
      const y = row * (loadedPNG.height + paddingY) + paddingY;  
      ctx.drawImage(loadedPNG, x, y, loadedPNG.width, loadedPNG.height);  
    }  
    const dataURL = canvas.toDataURL('image/png', 1);  
    const blob = dataURLToBlob(dataURL);  
  
    // Create a download link for the Blob  
    const link = document.createElement('a');  
    link.href = URL.createObjectURL(blob);  
    link.download = fileName;  
    link.click();  
  }, 100);  
}  
  
// JEWELRY  
function generateJewelryCanvas(numFilesLimit, fileName) {  
  const files = document.getElementById('file-input').files;  
  if (files.length > numFilesLimit) {  
    alert(`Error: You can only select up to ${numFilesLimit} images.`);  
    return;  
  }  
  generatePreview();  
  setTimeout(() => {  
    const canvas = document.createElement('canvas');  
    const ctx = canvas.getContext('2d');  
  
    const canvasWidthInches = 24;  
    const dpi72 = 72.01558002 * 5;  
    const canvasWidth = canvasWidthInches * dpi72;  
  
    const numRows = Math.ceil(loadedPNGs.length / 2);  
  
    const paddingY = 100;  
    const canvasHeight = numRows * (loadedPNGs[0].height + paddingY) + paddingY;  
    canvas.width = canvasWidth;  
    canvas.height = canvasHeight;  
  
    for (let i = 0; i < loadedPNGs.length; i++) {  
      const loadedPNG = loadedPNGs[i];  
      const col = i % 2;  
      const row = Math.floor(i / 2);  
      const x = col * (canvasWidth / 2);  
      const y = row * (loadedPNG.height + paddingY) + paddingY;  
      ctx.drawImage(loadedPNG, x, y, loadedPNG.width, loadedPNG.height);  
    }  
    const dataURL = canvas.toDataURL('image/png', 1);  
    const blob = dataURLToBlob(dataURL);  
  
    // Create a download link for the Blob  
    const link = document.createElement('a');  
    link.href = URL.createObjectURL(blob);  
    link.download = fileName;  
    link.click();  
  }, 100);  
}  

// RINGS  
if (document.querySelector("#format-btn").innerText === "Rings") {  
  generateJewelryCanvas(50, 'rings.png');  
}  
  
// NCK01  
else if (document.querySelector("#format-btn").innerText === "One Name Neckless") {  
  generateJewelryCanvas(50, 'NCK01.png');  
}  
  
// NCK02 
else if (document.querySelector("#format-btn").innerText === "Two Name Neckless") {  
  generateJewelryCanvas(35, 'NCK02.png');  
}  
  
// NCK03  
else if (document.querySelector("#format-btn").innerText === "Three Name Neckless") {  
  generateJewelryCanvas(20, 'NCK03.png');  
}  
  
// NCK04 
else if (document.querySelector("#format-btn").innerText === "Four Name Neckless") {  
  generateJewelryCanvas(20, 'NCK04.png');  
}  



  // add more here

}




// Function to generate and display the preview of the final image
function generatePreview() {

  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');

  const exportButton = document.getElementById('export-button');
  exportButton.addEventListener('click', handleExportButtonClick);

  ctx.imageSmoothingEnabled = true;
  ctx.imageSmoothingQuality = 'high';

  const canvasWidth = 800;
  const canvasHeight = 1200; 
  canvas.width = canvasWidth;
  canvas.height = canvasHeight;

  const scaleFactor = Math.min(canvasWidth / 2400, canvasHeight / (loadedPNGs.length * 200));

  for (let i = 0; i < loadedPNGs.length; i++) {
    const loadedPNG = loadedPNGs[i];

    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = 20 + col * (400 + 20);
    const y = 20 + row * (200 * scaleFactor + 20);

    ctx.drawImage(loadedPNG, x, y, 400 * scaleFactor, 200 * scaleFactor);
  }

  // Convert the canvas to a data URL
  const dataURL = canvas.toDataURL('image/png');

  // Create an <img> element for previewing the final image
  const previewImage = document.createElement('img');
  previewImage.src = dataURL;
  previewImage.classList.add('preview-pdf');

  // Clear the preview area and append the preview image
  previewArea.innerHTML = '';
  previewArea.appendChild(previewImage);
}

// Function to convert data URL to Blob
function dataURLToBlob(dataURL) {  
  const binaryString = atob(dataURL.split(',')[1]);  
  const arrayBuffer = new ArrayBuffer(binaryString.length);  
  const view = new Uint8Array(arrayBuffer);  
  for (let i = 0; i < binaryString.length; i++) {  
    view[i] = binaryString.charCodeAt(i);  
  } 
  const blob = new Blob([arrayBuffer], { type: 'image/png' });  
  
  return blob;  
}  
