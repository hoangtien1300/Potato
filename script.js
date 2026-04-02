// Function to open the detailed view of a class
function openClassDetail(className) {
    const modal = document.getElementById('classModal');
    const title = document.getElementById('modalClassTitle');
    
    title.innerText = `Chi tiết lớp: ${className}`;
    modal.classList.add('show');
}

// Function to close the detailed view modal
function closeClassDetail() {
    const modal = document.getElementById('classModal');
    modal.classList.remove('show');
}

// Function to open Issues
function openIssues(dept, className, issueCount) {
    // Stop event propagation so row click isn't triggered
    if (event) {
        event.stopPropagation();
    }
    
    const modal = document.getElementById('issuesModal');
    const title = document.getElementById('modalIssuesTitle');
    const list = document.getElementById('issuesList');
    
    title.innerText = `Vấn đề: ${dept} - Lớp ${className}`;
    
    if (issueCount === 0 || !issueCount) {
        list.innerHTML = '<li>Không có vấn đề nào được ghi nhận. Tốt!</li>';
    } else {
        // mock some specific issues based on department
        let mockIssues = [];
        if (dept === 'Teacher') {
            mockIssues = [
                'Học viên A vắng mặt không phép.',
                'Giáo viên quên nhập điểm chuyên cần tuần.',
                'Bài tập về nhà nộp trễ so với deadline.'
            ];
        } else if (dept === 'Academic') {
            mockIssues = [
                'Chậm điểm bài test định kỳ.',
                '2 học viên dưới điểm trung bình.'
            ];
        } else if (dept === 'Operation') {
            mockIssues = [
                'Phụ huynh khiếu nại về cơ sở vật chất.',
                'Chưa thu đủ học phí đợt 2.'
            ];
        }
        
        list.innerHTML = '';
        for (let i = 0; i < issueCount; i++) {
            list.innerHTML += `<li><i class="fa-solid fa-circle-exclamation" style="color: var(--danger); margin-right: 8px;"></i>${mockIssues[i % mockIssues.length]}</li>`;
        }
    }
    
    modal.classList.add('show');
}

// Function to close Issues modal
function closeIssues() {
    const modal = document.getElementById('issuesModal');
    modal.classList.remove('show');
}

// Close the modal if clicking outside the content
window.addEventListener('click', function(event) {
    const classModal = document.getElementById('classModal');
    const issuesModal = document.getElementById('issuesModal');
    
    if (event.target === classModal) {
        closeClassDetail();
    }
    if (event.target === issuesModal) {
        closeIssues();
    }
});
