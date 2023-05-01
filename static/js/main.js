

const url ="http://127.0.0.1:5000";

document.addEventListener('DOMContentLoaded',function() {

    const solve_btn = document.getElementById('solve-btn');

    solve_btn.addEventListener('click',function(){
        try {
            let intable = getTableData();
            console.log(intable)
            let data = { table:intable }
            fetch(url+"/solve", 
            {
                method:"POST",
                headers: {
                    "Content-Type":"application/json",
                },
                body: JSON.stringify(data),
            })
                .then((response) => response.json())
                .then(data =>{
                    console.log(data);
                    displaySolvedTables(data["Tables"])
                })
            } catch(e) {
                console.log("Error on fetch call")
                console.log(e)
            }
    });

});
function getTableData(){

    arrTable = []
    for (let i=0; i<9;i++) {
        newRow=[]
        for(let j=0; j<9;j++){
            let cell = document.getElementById(`cell${i}${j}`);
            if(cell.value == ''){
                newRow.push(0)
            }
            else {
                newRow.push(parseInt(cell.value))
            }
        }
        arrTable.push(newRow)
    }
    return(arrTable)
}

function checkValidTable(){};
//Check all entries are not letters. 
//make sure there are no duplicates in a row column or square

function displaySolvedTables(tableData){

    const div = document.getElementById("solved-divs");

    for(k=0;k<tableData.length;k++){
        let tableDiv = document.createElement("div");
        tableDiv.classList.add("solved-div");

        let table = document.createElement("table")
        for(i=0;i<9;i++){
            let row = document.createElement("tr")
            for(j= 0;j<9;j++){
                let cell = document.createElement("td")
                cell.innerHTML = tableData[k][i][j]
                row.appendChild(cell)
            }
            table.appendChild(row)
        }
        tableDiv.appendChild(table)
        div.appendChild(tableDiv)
    }
}