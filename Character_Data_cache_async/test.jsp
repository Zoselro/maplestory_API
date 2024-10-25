<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    function sendData() {
        const characterName = $('#characterName').val();
        const worldName = $('#worldName').val();
        const difficulty = $('#difficulty').val();
        const job = $('#job').val();

        $.ajax({
            url: '/test.py',  // Flask 서버 URL
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                character_name: characterName,
                world_name: worldName,
                difficulty: difficulty,
                job: job
            }),
            success: function(response) {
                console.log("Dojang Floor: " + response.max_dojang_floor);
                console.log("Theseed Floor: " + response.max_theseed_floor);
            },
            error: function(xhr, status, error) {
                console.error("Error: " + error);
            }
        });
    }
</script>

<input type="text" id="characterName" placeholder="Character Name">
<input type="text" id="worldName" placeholder="World Name">
<input type="text" id="difficulty" placeholder="Difficulty">
<input type="text" id="job" placeholder="Job">
<button onclick="sendData()">Submit</button>