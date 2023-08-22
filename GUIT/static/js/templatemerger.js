
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



// Handle file input change event
function handleFileInputChange(event) {
  // Clear the preview area and loaded PNGs array
  previewArea.innerHTML = '';
  loadedPNGs.length = 0;

  // Get the selected files
  const files = event.target.files;

  // Counter to keep track of the loaded images
  let counter = 0;

  // Loop through the files
  for (let i = 0; i < files.length; i++) {
    const file = files[i];

    // Create a FileReader to read the file
    const reader = new FileReader();

    // Set up the FileReader onload event
    reader.onload = function (e) {
      // Create a new Image element
      const img = new Image();

      // Set the onload event for the image
      img.onload = function () {
        // Store the loaded PNG in the array
        loadedPNGs.push(img);

        // Increment the counter
        counter++;

        // Check if all images are loaded
        if (counter === files.length) {
          // Generate and display the preview of the final image
          generatePreview();
        }
      };

      img.src = e.target.result;

      // Append the image to the preview area
      previewArea.appendChild(img);
    };

    // Read the file as data URL
    reader.readAsDataURL(file);
  }
}

// Handle export button click event
function handleExportButtonClick() {
  
                               // DESK PLATES

  if (document.querySelector("#format-btn").innerText === "Desk Plates") {

  // Check if the number of selected files exceeds the limit
  const files = document.getElementById('file-input').files;
  if (files.length > 28) {
    alert('Error: You can only select up to 28 images.');
    return;
  }
    
  // Generate and display the preview of the final image
  generatePreview();

  // Wait for a short delay to ensure the preview is updated
  setTimeout(() => {
    // Create a canvas element to hold the combined PNGs
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');

    // Set the width and height of the canvas
    const canvasWidthInches = 24;
    const canvasHeightinches = 36;
    const dpi72 = 72.01558002 * 5;
    const canvasWidth = canvasWidthInches * dpi72;
    const canvasHeight = canvasHeightinches * dpi72;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    // Loop through the loaded PNGs and draw them onto the canvas
    for (let i = 0; i < loadedPNGs.length; i++) {
      const loadedPNG = loadedPNGs[i];

       // Calculate the position to draw the image on the canvas
       let x, y, width, height;
       if (i === 0) {
         x = 1.03 * dpi72;
         y = 0.93 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 1) {
         x = 15.38 * dpi72;
         y = 0.93 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 2) {
         x = 1.03 * dpi72;
         y = 3.446 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 3) {
         x = 15.38 * dpi72;
         y = 3.446 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 4) {
         x = 1.03 * dpi72;
         y = 5.962 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 5) {
         x = 15.38 * dpi72;
         y = 5.962 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 6) {
         x = 1.03 * dpi72;
         y = 8.478 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 7) {
         x = 15.38 * dpi72;
         y = 8.478 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 8) {
         x = 1.03 * dpi72;
         y = 10.994 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 9) {
         x = 15.38 * dpi72;
         y = 10.994 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 10) {
         x = 1.03 * dpi72;
         y = 13.51 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 11) {
         x = 15.38 * dpi72;
         y = 13.51 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 12) {
         x = 1.03 * dpi72;
         y = 16.026 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 13) {
         x = 15.38 * dpi72;
         y = 16.026 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 14) {
         x = 1.03 * dpi72;
         y = 18.542 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 15) {
         x = 15.38 * dpi72;
         y = 18.542 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 16) {
         x = 1.03 * dpi72;
         y = 21.058 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 17) {
         x = 15.38 * dpi72;
         y = 21.058 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 18) {
         x = 1.03 * dpi72;
         y = 23.574 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 19) {
         x = 15.38 * dpi72;
         y = 23.574 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 20) {
         x = 1.03 * dpi72;
         y = 26.09 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 21) {
         x = 15.38 * dpi72;
         y = 26.09 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 22) {
         x = 1.03 * dpi72;
         y = 28.606 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 23) {
         x = 15.38 * dpi72;
         y = 28.606 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 24) {
         x = 1.03 * dpi72;
         y = 31.122 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 25) {
         x = 15.38 * dpi72;
         y = 31.122 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 26) {
         x = 1.03 * dpi72;
         y = 33.638 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 27) {
         x = 15.38 * dpi72;
         y = 33.638 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 28) {
         x = 1.03 * dpi72;
         y = 36.154 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else if (i === 29) {
         x = 15.38 * dpi72;
         y = 36.154 * dpi72;
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       } else {
         x = i % 2 === 0 ? canvasWidth - (8 * dpi72) : canvasWidth / 24; // Adjust the x-coordinate
         y = Math.floor((i - 1) / 2) * (2 * dpi72) + canvasHeight / 36; // Adjust the y-coordinate
         width = 8.08 * dpi72;
         height = 2 * dpi72;
       }

    if (i < 28) {
      ctx.save();
      ctx.translate(x + width / 2, y + height / 2); // Orgin point
      ctx.rotate(Math.PI);
      ctx.scale(-1, 1);
      ctx.drawImage(loadedPNG, -width / 2, -height / 2, width, height);
      ctx.restore();
    } else {
      ctx.drawImage(loadedPNG, x, y, width, height);
    }
  }

    // Convert the canvas to a data URL
    const dataURL = canvas.toDataURL('image/png', 1);

    // Create a Blob from the data URL
    const blob = dataURLToBlob(dataURL);

    // Create a download link for the Blob
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'desk_plates.png';

    // Simulate a click on the link to trigger the download
    link.click();
  }, 100);
} 

  
                               // FLUTES

else if (document.querySelector("#format-btn").innerText === "Flutes") {

  // Check if the number of selected files exceeds the limit
  const files = document.getElementById('file-input').files;
  if (files.length > 10) {
    alert('Error: You can only select up to 10 images.');
    return;
  }

    // Generate and display the preview of the final image
    generatePreview();

    // Wait for a short delay to ensure the preview is updated
    setTimeout(() => {
      // Create a canvas element to hold the combined PNGs
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
  
      // Set the width and height of the canvas
      const canvasWidthInches = 18.504;
      const canvasHeightinches = 18.504;
      const dpi72 = 70.05406617 * 10;
      const canvasWidth = canvasWidthInches * dpi72;
      const canvasHeight = canvasHeightinches * dpi72;
      canvas.width = canvasWidth;
      canvas.height = canvasHeight;
  
      // Loop through the loaded PNGs and draw them onto the canvas
      for (let i = 0; i < loadedPNGs.length; i++) {
        const loadedPNG = loadedPNGs[i];
  
         // Calculate the position to draw the image on the canvas
         let x, y, width, height;
         if (i === 0) {
           x = 2.25 * dpi72;
           y = .95 * dpi72;
           width = 4.5 * dpi72;
           height = 1.5 * dpi72;
         } else if (i === 1) {
           x = 11.35 * dpi72;
           y = .95 * dpi72;
           width = 4.5 * dpi72;
           height = 1.5 * dpi72;
         } else if (i === 2) {
           x = 2.25 * dpi72;
           y = 4.75 * dpi72;
          width = 4.5 * dpi72;
          height = 1.5 * dpi72;
        } else if (i === 3) {
          x = 11.35 * dpi72;
          y = 4.75 * dpi72;
          width = 4.5 * dpi72;
          height = 1.5 * dpi72;
        } else if (i === 4) {
          x = 2.25 * dpi72;
          y = 8.55 * dpi72;
         width = 4.5 * dpi72;
         height = 1.5 * dpi72;
       } else if (i === 5) {
         x = 11.35 * dpi72;
         y = 8.55 * dpi72;
         width = 4.5 * dpi72;
         height = 1.5 * dpi72;
        } else if (i === 6) {
          x = 2.25 * dpi72;
          y = 12.35 * dpi72;
         width = 4.5 * dpi72;
         height = 1.5 * dpi72;
       } else if (i === 7) {
         x = 11.35 * dpi72;
         y = 12.35 * dpi72;
         width = 4.5 * dpi72;
         height = 1.5 * dpi72;
        } else if (i === 8) {
          x = 2.25 * dpi72;
          y = 16.15 * dpi72;
         width = 4.5 * dpi72;
         height = 1.5 * dpi72;
       } else if (i === 9) {
         x = 11.35 * dpi72;
         y = 16.15 * dpi72;
         width = 4.5 * dpi72;
         height = 1.5 * dpi72;
        
         } else {
           x = i % 2 === 0 ? canvasWidth - (8 * dpi72) : canvasWidth / 18.504; // Adjust the x-coordinate
           y = Math.floor((i - 1) / 2) * (2 * dpi72) + canvasHeight / 18.504; // Adjust the y-coordinate
           width = 4.5 * dpi72;
           height = 1.5 * dpi72;
         }
  
      if (i < 10) {
        ctx.save();
        ctx.translate(x + width / 2, y + height / 2); // Orgin point
        ctx.rotate(Math.PI);
        ctx.drawImage(loadedPNG, -width / 2, -height / 2, width, height);
        ctx.restore();
      } else {
        ctx.drawImage(loadedPNG, x, y, width, height);
      }
    }
  
      // Convert the canvas to a data URL
      const dataURL = canvas.toDataURL('image/png', 1);
  
      // Create a Blob from the data URL
      const blob = dataURLToBlob(dataURL);
  
      // Create a download link for the Blob
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'flutes.png';
  
      // Simulate a click on the link to trigger the download
      link.click();
    }, 100);
  }
}

// Function to generate and display the preview of the final image
function generatePreview() {
  // Create a canvas element to hold the combined PNGs
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');

  // Add the event listener for the Export button outside the DOMContentLoaded event
  const exportButton = document.getElementById('export-button');
  exportButton.addEventListener('click', handleExportButtonClick);

  // Enable image smoothing and set the interpolation method to Lanczos
  ctx.imageSmoothingEnabled = true;
  ctx.imageSmoothingQuality = 'high';

  // Set the width and height of the canvas
  const canvasWidth = 800; // Adjust as needed for preview size
  const canvasHeight = 1200; // Adjust as needed for preview size
  canvas.width = canvasWidth;
  canvas.height = canvasHeight;

  // Calculate the scale factor for the preview
  const scaleFactor = Math.min(canvasWidth / 2400, canvasHeight / (loadedPNGs.length * 200));

  // Loop through the loaded PNGs and draw them onto the canvas
  for (let i = 0; i < loadedPNGs.length; i++) {
    const loadedPNG = loadedPNGs[i];

    // Calculate the position to draw the image on the canvas
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = 20 + col * (400 + 20); // Adjust as needed for preview size
    const y = 20 + row * (200 * scaleFactor + 20); // Adjust as needed for preview size

    // Draw the image on the canvas with the desired width and height
    ctx.drawImage(loadedPNG, x, y, 400 * scaleFactor, 200 * scaleFactor); // Adjust as needed for preview size
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
  const arr = dataURL.split(',');
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new Blob([u8arr], { type: mime });
}

