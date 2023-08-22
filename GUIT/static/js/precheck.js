

let parsedCsvData;  
let rowCount = 0;  
  
function handleFileSelect(evt) {  
    const file = evt.target.files[0];  
    Papa.parse(file, {  
        complete: function (results) {  
            console.log("CSV Parsed:", results.data);  
            parsedCsvData = results.data;  
            $('#output').html(generateTableHtml(results.data));  
            $('#preview-modal').modal('toggle');  
        }  
    });  
}  
  
function getPersonalization(options) {  
    const lines = options.split(/(?:\\n|\\r\\n|\\r)/g);  
    console.log("Options lines:", lines);  
    const personalizationKeywords = ['Personalization:', 'Personalization'];  
    const personalizations = [];  
  
    for (const line of lines) {  
        for (const keyword of personalizationKeywords) {  
            if (line.includes(keyword)) {  
                const startPos = line.indexOf(keyword) + keyword.length;  
                const personalization = line.slice(startPos).replace(/(^"|"$)/g, '').trim();  
                console.log("Found personalization:", personalization);  
                const splitPersonalization = personalization.split(/(?:\n|\r\n|\r)/g);  
  
                if (splitPersonalization.length === 1) {  
                    personalizations.push(splitPersonalization[0], "");  
                } else {  
                    personalizations.push(...splitPersonalization);  
                }  
  
                console.log("Line 1:", personalizations[personalizations.length - 2]);  
                console.log("Line 2:", personalizations[personalizations.length - 1]);  
            }  
        }  
    }  
    console.log("Final personalizations:", personalizations);  
    return personalizations;  
}  

function generateTableHtml(data) {  
    const indicesToDisplay = [0, 1, 2, 3];  
    rowCount = 0;  
    let tableHtml = '<table class="table table-bordered">';  
    for (let i = 0; i < data.length; i++) {  
        const row = data[i];  
        if (i === 0) {  
            tableHtml += '<thead><tr>';  
            for (let j = 0; j < row.length; j++) {  
                if (indicesToDisplay.includes(j)) {  
                    tableHtml += '<th>' + row[j] + '</th>';  
                }  
            }  
            tableHtml += '</tr></thead><tbody>';  
        } else {  
            if (row.includes("Discount")) {  
                tableHtml += '<tr class="separator"><td colspan="6"></td></tr>';  
                continue;  
            }  
            rowCount++;  
            tableHtml += '<tr>';  
            for (let j = 0; j < row.length; j++) {  
                if (indicesToDisplay.includes(j)) {  
                    if (j === 3) {  
                        const personalizations = getPersonalization(row[j]);  
                        if (personalizations.length === 0) {  
                            tableHtml += '<td><input type="text" class="personalization-input line1-input" value="" data-row-index="' + i + '"></td><td><input type="text" class="personalization-input line2-input" value="" data-row-index="' + i + '"></td>';  
                        } else if (personalizations.length === 1) {  
                            tableHtml += '<td><input type="text" class="personalization-input line1-input" value="' + personalizations[0] + '" data-row-index="' + i + '"></td><td><input type="text" class="personalization-input line2-input" value="" data-row-index="' + i + '"></td>';  
                        } else {  
                            tableHtml += '<td><input type="text" class="personalization-input line1-input" value="' + personalizations[0] + '" data-row-index="' + i + '"></td><td><input type="text" class="personalization-input line2-input" value="' + personalizations[1] + '" data-row-index="' + i + '"></td>';  
                        }  
                    } else {  
                        tableHtml += '<td>' + row[j] + '</td>';  
                    }  
                }  
            }  
            tableHtml += '</tr>';  
        }  
    }  
    tableHtml += '</tbody></table>';  
    return tableHtml;  
}  
 
$("#csv-file").on("change", handleFileSelect);  
  
let saveButtonClicked = false;  
  
$('#save-changes-btn').on('click', function () {  
    saveButtonClicked = true;  
    $('#preview-modal').modal('hide');  
});  
  
$('#preview-modal').on('hidden.bs.modal', function () {  
    if (saveButtonClicked) {  
        const line1Inputs = document.getElementsByClassName('line1-input');  
        const line2Inputs = document.getElementsByClassName('line2-input');  
  
        for (let i = 0; i < line1Inputs.length; i++) {  
            const rowIndex = parseInt(line1Inputs[i].getAttribute('data-row-index'));  
            const line1Value = line1Inputs[i].value;  
            const line2Value = line2Inputs[i].value;  
          
            const row = parsedCsvData[rowIndex];  
            const optionsIndex = 3;  
          
            const originalOptions = row[optionsIndex];
            const updatedPersonalization = [line1Value, line2Value].filter(val => val).join('\n');
            const newOptions = originalOptions.replace(/(Personalization:)([^,]*)(,|$)/, `$1${updatedPersonalization}$3`);  
          
            row[optionsIndex] = newOptions;  
        }  
        
  
        const updatedCsv = Papa.unparse(parsedCsvData); 
  
        const blob = new Blob([updatedCsv], { type: "text/csv;charset=utf-8;" });  
        const downloadLink = document.createElement("a");  
        const url = URL.createObjectURL(blob);  
        downloadLink.href = url;  
        downloadLink.setAttribute("download", "updated_csv.csv");  
        document.body.appendChild(downloadLink);  
        downloadLink.click();  
        document.body.removeChild(downloadLink);  
  
        saveButtonClicked = false;  
    }  
});  