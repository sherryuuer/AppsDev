####### 連結リストに関する：https://algo-logic.info/linked-list/
####### 方法１：連結リストの長さを計算してから、中央のタグを探し出してから、中央タグから対象の連結リストを出す。
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def lengt(head):
        count = 0
        while head:
            head = head.next
            count +=1
        return count
    tag = lengt(head) // 2
    for i in range(tag):
        head = head.next
    return head

####### 方法２：指針移動によって、早いのと遅いのがあって、速いのが2歩移動すると遅いのは1歩移動するという方法で、遅いほうを出すと結果になる。
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
