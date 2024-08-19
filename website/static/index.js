function deletePost(noteId) {
    fetch("/madlibs/delete-post", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/madlibs";
    });
  }

function choosePost(postId) {
    fetch("/create/choose", {
      method: "POST",
      body: JSON.stringify({ postId: postId }),
    }).then((_res) => {
      window.location.href = "/madlibs";
    });
}