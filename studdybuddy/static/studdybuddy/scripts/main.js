// filters out profiles on profile_list page
function profileSearch() {
  // Declare variables
  var input, filter, ul, profiles, classFields, i, j, otherProfileCourse;
  var classMatch = false;
  var profileFound = false;
  input = document.getElementById('searchbar');
  filter = input.value.toUpperCase();
  ul = document.getElementById("profile-list");
  profiles = ul.getElementsByClassName("profile-card");
  message = document.getElementById("none-found");

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < profiles.length; i++) {
    classMatch = false;
    classFields = profiles[i].getElementsByClassName("hidden-course");
    // no input in dropdown
    if (filter == "") {
        profiles[i].style.display = "none";
        message.style.display = "none";
    }
    // input in dropdown
    else {   
        for (j=0; j<classFields.length; ++j) {
            otherProfileCourse = classFields[j].value
            // if profile found with this class
            if (filter == otherProfileCourse) {
                classMatch = true;
                profileFound = true;
            }
        }
        // profile found with class
        if (classMatch) {
            profiles[i].style.display = "";
        }
        // no profiles found with class
        else {
            profiles[i].style.display = "none";
        }
        if (profileFound) {
            message.style.display = "none"
        }
        else {
            message.style.display = "";
            message.innerText = "No profiles found for " + filter;
        }
    }
  }
}

function addClass(newCourse) {
    // Declare variables
    var ul, courses, existing_course;
    var isAdded = false;
    // input = document.getElementById('searchbar');
    // filter = input.value.toUpperCase();
    ul = document.getElementById("added-courses");
    courses = ul.getElementsByClassName("course-card");


    // check if course already added
    // i += 2 to skip over br and hidden input elements in ul
    for (var i=0; i<ul.children.length; i += 3) {
        // this is the text of the card title for the courses already in the list
        existing_course = ul.children[i].children[0].children[0].children[0].innerText;
        if (existing_course === newCourse) {
            isAdded = true;
        }
    }

    if (!isAdded) {    
        // create all of the components of the displayed course card
        var li = document.createElement("li");
        li.id = newCourse;

        var card = document.createElement("div");
        card.classList.add("card")

        var cardBody = document.createElement("div");
        cardBody.classList.add("row");
        cardBody.classList.add("card-body");

        var col1 = document.createElement("div");
        col1.classList.add("col-md-10");

        var cardTitle = document.createElement("span");
        cardTitle.classList.add("card-title");
        cardTitle.innerText = newCourse;

        var col2 = document.createElement("div");
        col2.classList.add("col-md-2");

        var closeBtn = document.createElement("button");
        closeBtn.classList.add("btn-close")
        closeBtn.setAttribute("type", "button");
        closeBtn.setAttribute("aria-label", "Close");
        closeBtn.style.color = "darkred";
        closeBtn.innerText = "X";

        var hiddenInput = document.createElement("input");
        hiddenInput.setAttribute("type", "hidden");
        hiddenInput.name = newCourse;

        var br = document.createElement("br");

        // add card to added courses ul
        col1.append(cardTitle);
        col2.append(closeBtn);
        cardBody.append(col1);
        cardBody.append(col2);
        card.append(cardBody);
        li.append(card);
        ul.append(li);
        ul.append(hiddenInput);
        ul.append(br);
    }
}

function removeClass() {
    // removes li and br element from added classes ul
    var li = this.parentElement.parentElement.parentElement.parentElement;
    var br = li.nextElementSibling;
    li.remove();
    br.remove();
}

var classSelect = document.getElementById('edit-classes-searchbar');
classSelect.addEventListener('change', function() {
    var newCourse = this.value;
    addClass(newCourse);
});

var courseCards = document.getElementsByClassName('btn-close');
for (var i=0; i<courseCards.length; ++i) {
    courseCards[i].addEventListener('click', removeClass);
}


