
// show or hide the work-where div based on the worked-before checkbox
$(document).ready(function() {
    $('#worked-before').change(function() {
        if ($(this).is(':checked')) {
            $('#work-where').show();
        } else {
            $('#work-where').hide();
        }
    });
});

// add new entry when add button clicked and remove one when remove button clicked

const container = document.getElementsByClassName('entry-container');

let forms = 1;
const maxForms = 25;

function updateButtons() {
    if (forms == 1) {
        document.getElementById('removeEmployment').style.display = 'none';
    } else {
        document.getElementById('removeEmployment').style.display = 'block';
    }

    if (forms >= maxForms) {
        document.getElementById('addEmployment').style.display = 'none';
    } else {
        document.getElementById('addEmployment').style.display = 'block';
    }
}

function addButtonClick() {
    if (forms >= maxForms) {
        return false;
    }
    const newEntry = document.createElement('div');
    newEntry.innerHTML = `
    <div class="work-entry">
    <div class="split" style="margin-bottom: 0px;">
        <div class="split">
            <div class="split-item">
                <p>From</p>
                <input type="date" id="start" name="employmentfrom${forms}" min="2023-12-24" max="2030-01-01"/>
            </div>
            <div class="split-item">
                <p>Until</p>
                <input type="date" id="start" name="employmentto${forms}" min="2023-12-24" max="2030-01-01"/>
            </div>
        </div>
        <div class="bottomanchor">
            <input type="text" name="employer${forms}" placeholder="Company Name">
        </div>
    </div>

    <div class="phone-container">
        <input type="number" name="phoneAreaCode${forms}" id="code" placeholder="1+">
        <input type="number" 
            name="phoneNumber${forms}" 
            id="number" 
            placeholder="123-45-678"
        >
    </div>

    <div class="split" style="margin-top: 10px;">
        <!--Supervisor name & position-->
        <input type="text" name="supervisorname${forms}" placeholder="Supervisor Name">
        <input type="text" name="supervisorposition${forms}" placeholder="Supervisor Position">
    </div>
    
    <div class="split">
        <!--Start Salary & end Salary & position-->
        <input type="number" name="startSalary${forms}" placeholder="Start Salary">
        <input type="number" name="endSalary${forms}" placeholder="End Salary">
        <input type="text" name="position${forms}" placeholder="Position">
    </div>

    <!--Reason for leaving-->
    <input type="text" name="reason${forms}" placeholder="Reason for leaving">
    <hr>
</div>
    `;
    container[0].appendChild(newEntry);
    forms += 1;

    updateButtons()
    return false
};

function removeButtonClick() {
    const lastDiv = container[0].lastElementChild;
    if (lastDiv) {
        container[0].removeChild(lastDiv);
        forms -= 1;
    }

    updateButtons()
    return false
};

//submit button stuff
function submit1() {
    document.getElementById("submitfirst").style.display = "none";
    document.getElementById("areyousure").style.display = "block";
    return false
}

function noconfirm() {
    document.getElementById("submitfirst").style.display = "block";
    document.getElementById("areyousure").style.display = "none";
    return false
}

//wait for loaded
document.addEventListener('DOMContentLoaded', updateButtons, false);

