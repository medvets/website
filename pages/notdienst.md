title: Aktueller Notdienst

Der Notdienst gilt immer für den Feiertag bzw. das Wochenende in der laufenden Kalenderwoche.
Die Notdienstzeit beginnen am Wochenende am Freitag um 18 Uhr und endet am Montag um 9 Uhr.
An Feiertagen beginnt der Notdienst am Vortag des Feiertags um 18 Uhr und dauert bis zum Tag nach dem Feiertag um 9 Uhr.


Praxis Finkbeiner <small>(31.12.2014-01.01.2015, 26.01.2015-01.02.2015, 16.03.2015-22.03.2015, 20.04.2015-26.04.2015, 14.05.2015, 18.05.2015-24.05.2015, 15.06.2015-21.05.2015, 27.07.2015-02.08.2015, 14.09.2015-20.08.2015, 19.10.2015-25.10.2015, 12.12.2015, 14.12.2015-20.12.2015)</small>
-----------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/finkbeiner.html)

Praxis Leis <small>(25.12.2014-26.12.2014, 19.01.2015-25.01.2015,09.03.2015-15.03.2015, 27.04.2015-03.05.2015, 25.05.2015-31.05.2015, 13.07.2015-19.07.2015, 17.08.2015-23.08.2015, 21.09.2015-27.09.2015, 26.10.2015-01.11.2015, 30.11.2015-06.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/leis.html)


Praxis Anton <small>(24.12.2014, 03.01.2015-04.01.2015, 16.02.2015-22.02.2015, 13.04.2015-19.04.2015, 11.05.2015-17.05.2015, 01.06.2015-07.06.2015, 20.07.2015-26.07.2015, 07.09.2015-13.09.2015, 05.10.2015-11.10.2015, 23.11.2015-29.11.2015, 21.12.2015-27.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/anton.html)

Praxis Wolandowitsch <small>(05.01.2015-11.01.2015,02.03.2015-08.03.2015, 05.04.2015-06.04.2015, 01.05.2015, 25.05.2015, 22.06.2015-28.06.2015, 10.08.2015-16.08.2015, 28.09.2015-04.10.2015, 13.12.2015, 31.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/wolandowitsch.html)

Praxis von Götz <small>(12.01.2015-18.01.2015, 06.05.2015-10.05.2015, 06.07.2015-12.07.2015 )</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/von goetz.html)

Praxis Bachmann <small>(27.12.2014-28.12.2014, 02.02.2015-08.02.2015, 23.02.2015-01.03.2015, 23.03.2015-29.03.2015,07.04.2015-12.04.2015, 29.06.2015-05.07.2015, 03.08.2015-09.08.2015, 31.08.2015-06.09.2015, 12.10.2015-18.10.2015, 16.11.2015-22.11.2015, 24.12.2015-25.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/bachmann.html)

Praxis Schmöe <small>(09.02.2015-15.02.2015, 03.04.2015-04.04.2015, 08.06.2015-14.06.2015, 24.08.2015-30.08.2015, 02.11.2015-08.11.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/schmoe.html)


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
