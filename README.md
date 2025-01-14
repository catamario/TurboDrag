| ![application](https://github.com/user-attachments/assets/6cbb6405-b523-428d-b97b-83bc1a3dfe52) | 
|----------------------------------------------------------------------------------------------------|
| This program is a competitive application designed for multiple users within an interface. Each participant competes to be the first to extract the most valuable item from an inventory. The program utilizes an automated "click-drag-release" algorithm, which searches and locates images on the screen, moves the mouse accurately, and presses buttons quickly and efficiently to drag the precious item into their possession. |
| By using multiple threads, the application optimizes the search and extraction process, creating a fast-paced and intense experience. |

<table align="center">
  <tr>
    <td><img src="https://github.com/user-attachments/assets/4fb1879c-9d9c-4ead-be69-b6d4dd3f6efb" width="200" /></td>
    <td><img src="https://github.com/user-attachments/assets/8723862b-4fc8-4c2d-b379-44d9aec2599a" width="300" /> <br></br>
    <p style="text-align:center;">Traditional method of dragging item into<br>inventory without TurboDrag</p></td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="https://github.com/user-attachments/assets/42749290-ef48-49a8-9036-922dd15abefc" width="500" />
      <p style="text-align:center;">Method of dragging items into inventory using TurboDrag</p>
    </td>
  </tr>
</table>


| **Feature**               | **Description**                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Object Detection**       | I used image recognition to locate specific objects on the screen by comparing screenshots stored in a defined folder. The program utilizes **pyautogui** and the **`locateOnScreen()`** function to search for images within a given region of the screen. The images are stored in a folder, and the program iterates through them to find matching objects on the screen with a specified confidence level. Once an object is detected, the program calculates its position, moves the cursor to it, performs a drag-and-drop action, and releases the mouse button. This process ensures a precise and efficient way to interact with the screen. |
| **Keyboard Listening**     | I implemented **pynput.keyboard** to monitor key presses and provide a toggle to start or stop the object search process. This functionality is useful to pause between search cycles and prevent CPU overload. For example, when there are no objects to search for, the program can be temporarily paused to save resources.                                          |
| **Defined Search Regions** | To optimize performance, I defined search regions on the screen, limiting the area in which the program searches for objects. Instead of performing a full-screen search, the search is constrained to specific areas (slots of interest), which significantly reduces processing time and speeds up the search.                                                       |
| **Threading for Efficiency** | I utilized **multithreading** (running multiple functions simultaneously) to speed up the object search. The program looks for 18 objects in total, dividing this task into 3 threads (using **`threading`** in Python). Each thread handles a specific set of images, creating a more efficient system and reducing search time. For example, the first thread searches objects 1-6, the second thread searches objects 7-12, and the third thread searches objects 13-18. |
| **Layered Architecture**   | The program is built using a **layered architecture**, which improves modularity and code maintainability. The application is structured as follows: <br> **UI** (User Interface): Allows the user to interact with the application. <br> **Operations** (Script Code): Contains the main logic of the application, such as searching and identifying objects. <br> **Targets** (Searched Images): These are the reference images that need to be recognized on the screen. <br> **Arguments** (Defined Parameters): Parameters are managed separately to allow easy adjustment of the application's behavior.  |
