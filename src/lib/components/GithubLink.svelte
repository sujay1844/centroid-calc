<script>
  export let link = 'https://github.com/sujay1844/centroid-calc';
</script>

<style>
  .github-button {
    position: fixed;
    top: 20px;
    right: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 16px;
    background-color: black;
    color: white;
    border: none;
    border-radius: 4px;
    font-family: Arial, sans-serif;
    font-size: 16px;
    cursor: pointer;
    z-index: 9999;
  }

  .github-button:hover {
    background-color: #24292e;
  }
</style>

<section>
  <a class="github-button" href={link} target="_blank">
		<img src="github-mark-white.svg" alt="GitHub" width="24" height="24" />

		<span style="margin-left: 8px;">View on GitHub</span>
	</a>
</section>