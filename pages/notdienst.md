title: Aktueller Notdienst

Praxis Leis <hr/> (09.08.2014, 10.08.2014, 24.12.2014, 31.12.2014, 01.01.2015)
------------------------------------------------------------------------------

Adresse
12345 Haste

1938 913209127309 718237

[Mehr informationen über die Praxis](tieraerzte/arzt2.html)

Praxis Kitty Wash (2014-01-01 - 2014-01-07)
---------------------------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



<!-- ACHTUNG, AB HIER NICHT MODIFIZIEREN!
Es sei denn, Sie wissen was Sie tun :-)
Der nachfolgende JavaScript-Code wird nach dem Laden dieser Seite auf dem
Computer des Nutzers ausgeführt und zeigt den jeweils gültigen Notdienst an
und versteckt die restlichen Inhalte, wenn das Datum nicht passt.
Die Zeiträume werden in Klammern in den Überschriften der ersten beiden
Stufen angegeben (also z.B. `# Text (23.04.2014, 01.05.2014)`).
Mehrere Datumsangaben werden durch Komma getrennt. Es ist auch möglich
Zeiträume anzugeben, wobei ein Bindestrich das Start- vom End-Datum
abgrenzt. Beispiel `# Text (23.04.2014 - 25.04.2014)`. Die Leerzeichen um
den Bindestrich sind wichtig.
Die Datumsangaben selber werden kodiert nach ISO 8601 (wobei deutsche
Monatsnamen akzeptiert werden):
http://en.wikipedia.org/wiki/ISO_8601#Week_dates

(C) 2014, Samuel John (www.samueljohn.de)
Release under MIT license version.
-->
<script src="moment.js"></script>
<script>
// Find html nodes on the same level after elem, up to but excluding the
// next element in the array `stop_tags`
function siblings_up_to (elem, stop_tags) {
    var content = [];
    do {
        content.push(elem);
        elem = elem.nextElementSibling;
    } while (elem && stop_tags.indexOf(elem.tagName) < 0);
    return content;
}

function hide(element) {
    element.style.display = "None";
}

function extract_dates (text) {
    // Return a list of pairs of moment.js objects `[ ...,[start, end],...]`
    // var text = "foo (har) bar (KW02, KW06, 27. Mai 2014, KW10 - KW14)"
    var dates = [];
    var find_text_in_last_brackets_regex = /^.*\((.*)\)$/gm;
    var text_in_last_brackets = find_text_in_last_brackets_regex.exec(text);
    console.log("text_in_last_brackets: ", text_in_last_brackets);
    if (text_in_last_brackets && text_in_last_brackets.length > 1) {
        // if match, split out possible multiple dates seperated by `,`
        var date_ranges = text_in_last_brackets[1].split(',');
        date_ranges.forEach(
            function (one_date_range_text) {
                var from_to = one_date_range_text.split('-');
                // try to parse start...
                console.log("from,to (string): " + from_to);
                var start = moment(from_to[0], "DD.MM.YYYY", "de", true);
                var end = start.clone();
                if (start.isValid) {
                    console.log("...is valid.");
                    end.add('d', 1);  // so that 01.02.2014 - 02.02.2014 includes 02.02
                }
                // if even the KW parsing attempt failed, we continue to the next
                // Check if there is a stop-date
                if (from_to.length > 1) {
                    end = moment(from_to[1]);
                    end.add('d', 1);  // so that 01.02.2014 - 02.02.2014 includes 02.02
                }
                dates.push([start, end]);
            }
        )
    }
    return dates;
}


function seek_and_hide () {
    var h2_headings = document.getElementById("content").getElementsByTagName("H2");
    h2_headings.forEach(function process_section (elem) {
        extract_dates(elem.textContent).forEach(function (date) {
            if (date.length <= 0) { return; }
            var start = date[0];
            var end = date[1];
            var now = moment();
            if (now >= start && now <= end) {
                return; // don't hide this, let it stay visible
            } else {
                siblings_up_to (elem, ["H2"]).forEach( function (el) {
                    hide(el);
                })
            }

        });
    });
}

document.onload = seek_and_hide;

// moment("2014-02-01", ["[KW]W", "[KW]WW", moment.ISO_8601], 'de', true);
// moment("2014-W30").add("days", 7)

// first make all hidden
// Onload?
//    find headings and all up to next heading of level #
//    get current date and the week nr
//    parse (KW X[, Y]...)
//    display (unhide) all headings that are in this current week
</script>