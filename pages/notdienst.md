title: Aktueller Notdienst

Der Notdienst gilt immer für den Feiertag bzw. das Wochenende in der laufenden Kalenderwoche.


Praxis Kitty Wash <small>(4. Aug. 2014, 8. Aug. 2014)</small>
-----------------------------------------------------------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Praxis Leis <small>(01.11.2014-07.11.2014, 24.12.2014, 31.12.2014 - 01.01.2015, 01. Aug. 2014 - 10.08.2014)</small>
-------------------------------------------------------------

Adresse
12345 Haste

1938 913209127309 718237

[Mehr informationen über die Praxis](tieraerzte/arzt2.html)





<!--              ACHTUNG, AB HIER NICHT MODIFIZIEREN!

Es sei denn, Sie wissen was Sie tun :-)

Der nachfolgende JavaScript-Code wird nach dem Laden dieser Seite auf dem
Computer des Nutzers ausgeführt und zeigt den jeweils gültigen Notdienst an
und versteckt die restlichen Inhalte, wenn das Datum nicht passt.
Die Zeiträume werden in Klammern in den Überschriften der ersten beiden
Stufen angegeben (also z.B. `# Text (23.04.2014, 01.05.2014)`).
Mehrere Datumsangaben werden durch Komma getrennt. Es ist auch möglich
Zeiträume anzugeben, wobei ein Bindestrich das Start- vom End-Datum
abgrenzt. Beispiel `# Text (23.04.2014 - 25.04.2014)`.
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

function parse_date (text) {
    return moment(text, ["DD.MM.YYYY", "DD. MMM YYYY"], "de");
}

function extract_dates (text) {
    // Return a list of pairs of moment.js objects `[ ...,[start, end],...]`
    var dates = [];
    var find_text_in_last_brackets_regex = /^.*\((.*)\)$/gm;
    var text_in_last_brackets = find_text_in_last_brackets_regex.exec(text);
    console.log("regex matching: ", text_in_last_brackets);
    if (text_in_last_brackets && text_in_last_brackets.length > 1) {
        // if match, split out possible multiple dates seperated by `,`
        var date_ranges = text_in_last_brackets[1].split(',');
        console.log("date_ranges: " + date_ranges);
        date_ranges.forEach(
            function (one_date_range_text) {
                var from_to = one_date_range_text.split('-');
                console.log("from,to (string): " + from_to);
                if (from_to.length > 2) {
                    console.log("Warning: More than two '-' found in date range.");
                    return;
                }
                // try to parse start...
                var start = parse_date(from_to[0]);
                var end = start.clone();
                if (start.isValid) {
                    console.log("...start is valid.");
                    end.add('d', 1);  // so that 01.02.2014 - 02.02.2014 includes 02.02
                }
                // Check if there is a stop-date
                if (from_to.length > 1) {
                    console.log("Stop-date given: ", from_to[1]);
                    end = parse_date(from_to[1]);
                    end.add('d', 1);  // so that 01.02.2014 - 02.02.2014 includes 02.02
                }
                dates.push([start, end]);
            }
        )
    }
    return dates;
}

function now_in_date_ranges ( date_ranges ) {
    var i = 0;
    for (; i < date_ranges.length; i++) {
        var date = date_ranges[i];
        if (date.length <= 0) {
            console.log("Could not extract dates for " + heading);
            return;
        }
        var start = date[0];
        var end = date[1];
        var now = moment();
        console.log("start " + start._d);
        console.log("now " + now._d);
        console.log("end " + end._d);
        if (now >= start && now <= end) {
            console.log("keep this visible.");
            return true; // don't hide this, let it stay visible
        }
    }
    console.log("hide this.");
    return false;
}

function seek_and_hide () {
    var h2_headings = document.getElementById("content").getElementsByTagName("H2");
    console.log("seek and hide...");
    console.log("found " + h2_headings.length + " h2 headings.");
    var i = 0;
    for (; i < h2_headings.length; i++) {
        console.log("----------------- ", i );
        var heading = h2_headings[i];
        console.log("Processing " + heading.textContent);
        if (! now_in_date_ranges(extract_dates(heading.textContent))) {
            console.log(siblings_up_to(heading, ["H2", "H1"]));
            siblings_up_to(heading, ["H2", "H1"]).forEach( function (el) {
                el.style.display = "None";
            });
        }
        console.log("done. ", i);
    }
}

seek_and_hide();  // run this shit
</script>
